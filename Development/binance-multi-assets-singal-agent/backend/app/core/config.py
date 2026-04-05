import os
from dotenv import load_dotenv

# 從 .env 檔案載入環境變數
load_dotenv()

class Settings:
    BINANCE_API_KEY: str = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET: str = os.getenv("BINANCE_API_SECRET")
    # 使用測試網
    USE_TESTNET: bool = True

settings = Settings()