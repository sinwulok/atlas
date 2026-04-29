# binance-multi-assets-singal-agent

Binance 多資產交易訊號代理程式原型，包含後端與前端架構。  
Multi-asset Binance trading signal agent prototype with backend and frontend structure.

---

## 概述 | Overview

一個多資產加密貨幣交易機器人，使用 MACD 等技術指標在 Binance 上自動執行交易邏輯。機器人獲取歷史資料、套用交易策略，並在 Binance Testnet 上模擬或執行交易。  
A multi-asset crypto trading bot that uses technical indicators such as MACD to automate trading on Binance. This bot fetches historical data, applies trading logic, and simulates or executes trades on the Binance Testnet.

---

## 類別與狀態 | Category and Lifecycle

- **類別 | Category**：Development
- **類型 | Type**：Quant | Signal | Feature Extraction
- **生命週期 | Lifecycle**：stable
- **標籤 | Tags**：trading, quant, binance, agent

---

## 結構 | Structure

```text
Development/binance-multi-assets-singal-agent/
├── backend/                  # Python FastAPI 專案 | Python FastAPI project
│   ├── app/
│   │   ├── api/              # API 端點 | API endpoints
│   │   │   ├── endpoints/
│   │   │   │   └── bot_control.py  # 控制機器人啟動/停止/狀態的 API
│   │   │   └── websocket.py        # WebSocket 即時通訊端點
│   │   ├── core/
│   │   │   └── config.py           # 讀取 API 金鑰和設定
│   │   ├── services/
│   │   │   ├── binance_service.py  # 封裝幣安 API 互動（OOP）
│   │   │   ├── indicator_service.py # 技術指標計算（MACD 等）
│   │   │   └── trading_bot.py      # 核心交易機器人邏輯（OOP Class）
│   │   └── main.py                 # FastAPI 應用程式進入點
│   ├── .env                        # API 金鑰（請勿上傳至 Git）
│   └── requirements.txt
├── frontend/                 # React 專案 | React project
│   ├── src/
│   │   ├── api/
│   │   │   └── botApi.js           # 呼叫後端 API 的函式
│   │   ├── components/
│   │   │   ├── BotController.js    # 開始/停止按鈕元件
│   │   │   ├── Dashboard.js        # 主儀表板
│   │   │   ├── LogStream.js        # 即時日誌元件
│   │   │   └── AssetStatus.js      # 各資產狀態元件
│   │   ├── hooks/
│   │   │   └── useWebSocket.js     # WebSocket 連線自訂 hook
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

---

## 如何執行 | How to Run

1. 安裝相依套件 | Install required packages:
   ```sh
   pip install -r requirements.txt
   ```

2. 在 `.env` 檔案中設定 Binance API 金鑰 | Configure Binance API keys in `.env`:
   ```
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_api_secret
   ```

3. 執行交易機器人 | Run the trading bot:
   ```sh
   python -m main_agent
   ```

4. 依照提示輸入 API 資訊並設定資產。  
   Follow the prompts to enter your API information and configure your assets.

---

## 相依項目 | Dependencies

- Python FastAPI（後端 | backend）
- React（前端 | frontend）
- python-binance
- pandas、MACD 指標函式庫

---

## 輸出與展示 | Outputs and Demos

### MACD 指標圖 | MACD Indicator Chart
![MACD 指標圖](pubclic/assets/macd-of-closing.png)

### BTCUSDT 收盤價與訊號 | BTCUSDT Closing Price with Signals
![BTCUSDT Closing Price with Signals](pubclic/assets/BTCUSDT-closing-price-with-signals.png)

---

## 注意事項 | Notes and Limitations

- 本專案為交易機器人原型，請勿在真實帳戶中直接使用。This is a trading bot prototype; do not use directly with real accounts.
- 需要有效的 Binance API 金鑰，測試建議使用 Binance Testnet。Requires valid Binance API keys; use Binance Testnet for testing.
- `.env` 檔案含有 API 金鑰，請勿上傳至 Git。The `.env` file contains API keys — do not commit to Git.
- 可從 `.csv` 或 `.txt` 檔案匯入資產清單。Option to import asset data from .csv or .txt files.

---

## 相關連結 | Related Links

- [Binance API (python-binance)](https://github.com/sammchardy/python-binance)
- [專案 Catalog | Project Catalog](../../catalog/index.md)
- [Repository 根目錄 | Repository Root](../../README.md)
