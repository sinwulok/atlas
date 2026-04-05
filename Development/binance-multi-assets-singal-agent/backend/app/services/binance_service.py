from binance.client import Client
from app.core.config import settings

class BinanceService:
    def __init__(self):
        self.client = Client(
            settings.BINANCE_API_KEY,
            settings.BINANCE_API_SECRET,
            testnet=settings.USE_TESTNET
        )

    def get_historical_klines(self, symbol: str, interval: str, start_str: str):
        return self.client.get_historical_klines(symbol, interval, start_str)

    def place_market_buy_order(self, symbol: str, quantity: float):
        try:
            order = self.client.order_market_buy(symbol=symbol, quantity=quantity)
            return {"success": True, "order": order}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def place_market_sell_order(self, symbol: str, quantity: float):
        try:
            order = self.client.order_market_sell(symbol=symbol, quantity=quantity)
            return {"success": True, "order": order}
        except Exception as e:
            return {"success": False, "message": str(e)}

# 建立一個單例，方便在其他地方使用
binance_service = BinanceService()