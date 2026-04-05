#!/bin/bash

# 取消定義專案根目錄名稱，讓腳本直接在當前目錄建立結構

echo "正在建立專案結構於: $(pwd)"

# 不再建立最外層的 BASE_PATH 目錄，直接在當前目錄操作

# 建立 backend 目錄及檔案
mkdir -p backend/app/api/endpoints
mkdir -p backend/app/core
mkdir -p backend/app/services

touch backend/app/__init__.py
touch backend/app/api/__init__.py
touch backend/app/api/endpoints/__init__.py
touch backend/app/api/endpoints/bot_control.py
touch backend/app/api/websocket.py
touch backend/app/core/__init__.py
touch backend/app/core/config.py
touch backend/app/services/__init__.py
touch backend/app/services/binance_service.py
touch backend/app/services/indicator_service.py
touch backend/app/services/trading_bot.py
touch backend/app/main.py
touch backend/.env
touch backend/requirements.txt

# 建立 frontend 目錄及檔案
mkdir -p frontend/public
mkdir -p frontend/src/api
mkdir -p frontend/src/components
mkdir -p frontend/src/hooks

touch frontend/public/index.html
touch frontend/src/api/botApi.js
touch frontend/src/components/BotController.js
touch frontend/src/components/Dashboard.js
touch frontend/src/components/LogStream.js
touch frontend/src/components/AssetStatus.js
touch frontend/src/hooks/useWebSocket.js
touch frontend/src/App.js
touch frontend/src/index.js
touch frontend/src/index.css
touch frontend/package.json

# 建立根目錄下的 README.md
touch README.md

echo ""
echo "專案結構已成功生成！"
