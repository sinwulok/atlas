import asyncio
from typing import List, Dict, Any
from app.api.websocket import log_broadcaster
from .binance_service import binance_service
from .indicator_service import indicator_service

class TradingBot:
    def __init__(self, assets: List[Dict[str, Any]]):
        self.assets_config = assets
        self.is_running = False
        self._task = None
        # 使用一個字典來追蹤每個資產的持倉狀態
        self.positions = {asset['asset']: asset['is_long'] for asset in assets}

    async def _log(self, message: str):
        print(message) # 在伺服器端打印
        await log_broadcaster.broadcast(message) # 推送到前端

    async def _execute_trade_logic_for_asset(self, asset_info: Dict[str, Any]):
        asset = asset_info['asset']
        symbol = f"{asset}USDT"
        is_long = self.positions[asset]

        try:
            klines = binance_service.get_historical_klines(symbol, "1m", "1 hour ago UTC")
            bars = indicator_service.get_bars_with_indicators(symbol, klines)

            if bars.empty:
                await self._log(f"[{asset}] No data to process.")
                return

            last_bar = bars.iloc[-1]
            should_buy = last_bar['MACD'] > 0 and last_bar['Pct Change 30m'] > 0
            should_sell = last_bar['MACD'] < 0 and last_bar['Pct Change 30m'] < 0

            status_msg = f"[{asset}] Status: {'Long' if is_long else 'Not Long'}. Buy Signal: {should_buy}. Sell Signal: {should_sell}."
            await self._log(status_msg)

            if not is_long and should_buy:
                await self._log(f"[{asset}] BUY signal triggered. Placing market buy order.")
                result = binance_service.place_market_buy_order(symbol, asset_info['order_size'])
                if result.get("success"):
                    self.positions[asset] = True
                    await self._log(f"[{asset}] BUY order successful: {result['order']}")
                else:
                    await self._log(f"[{asset}] BUY order failed: {result['message']}")

            elif is_long and should_sell:
                await self._log(f"[{asset}] SELL signal triggered. Placing market sell order.")
                result = binance_service.place_market_sell_order(symbol, asset_info['order_size'])
                if result.get("success"):
                    self.positions[asset] = False
                    await self._log(f"[{asset}] SELL order successful: {result['order']}")
                else:
                    await self._log(f"[{asset}] SELL order failed: {result['message']}")

        except Exception as e:
            await self._log(f"[{asset}] An error occurred: {str(e)}")

    async def _run_loop(self):
        await self._log("Trading bot started.")
        while self.is_running:
            try:
                for asset_info in self.assets_config:
                    await self._execute_trade_logic_for_asset(asset_info)
                await self._log("--- Iteration complete ---")
                await asyncio.sleep(10) # 每 10 秒檢查一次
            except asyncio.CancelledError:
                await self._log("Bot loop cancelled.")
                break
            except Exception as e:
                await self._log(f"Critical error in main loop: {e}")
                await asyncio.sleep(30) # 發生嚴重錯誤時等待更長時間

    def start(self):
        if not self.is_running:
            self.is_running = True
            self._task = asyncio.create_task(self._run_loop())
            return {"status": "Bot started"}
        return {"status": "Bot is already running"}

    def stop(self):
        if self.is_running:
            self.is_running = False
            if self._task:
                self._task.cancel()
            self._task = None
            # 使用 asyncio.run_coroutine_threadsafe 如果在不同線程
            asyncio.create_task(self._log("Trading bot stopped by user."))
            return {"status": "Bot stopping"}
        return {"status": "Bot is not running"}

    def get_status(self):
        return {
            "is_running": self.is_running,
            "positions": self.positions
        }

# 從 Notebook 來的資產設定
initial_assets = [
    {'asset': 'BTC', 'is_long': False, 'order_size': 0.001}, # 調整 order size
    {'asset': 'ETH', 'is_long': False, 'order_size': 0.01},
    {'asset': 'LTC', 'is_long': False, 'order_size': 0.1},
]

# 建立機器人單例
trading_bot_instance = TradingBot(assets=initial_assets)