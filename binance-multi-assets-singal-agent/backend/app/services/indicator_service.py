import pandas as pd
import pandas_ta as ta

class IndicatorService:
    def get_bars_with_indicators(self, symbol: str, klines: list) -> pd.DataFrame:
        if not klines:
            return pd.DataFrame()

        df = pd.DataFrame(klines)
        df.columns = [
            "Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
            "Quote asset volume", "Number of trades", "Taker buy base asset volume",
            "Taker buy quote asset volume", "Ignore"
        ]

        df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
        df.set_index('Open time', inplace=True)
        
        # 只保留需要的欄位並轉換為數字
        df = df.iloc[:, :5]
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df.dropna(inplace=True)

        if df.empty or len(df) < 30: # 確保有足夠的數據來計算指標
            return df
            
        # 計算 MACD
        macd = ta.macd(df["Close"], fast=12, slow=26, signal=9)
        if macd is not None and not macd.empty:
            df['MACD'] = macd.iloc[:, -1] # 取 MACD 的信號線

        # 計算 30 分鐘價格變化百分比
        df['Pct Change 30m'] = df['Close'].pct_change(30)
        
        df.dropna(inplace=True)
        return df

indicator_service = IndicatorService()