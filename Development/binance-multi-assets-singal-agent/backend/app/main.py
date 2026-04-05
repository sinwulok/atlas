from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import bot_control
from app.api.websocket import websocket_endpoint

app = FastAPI(title="Binance Trading Bot API")

# 設定 CORS 中介軟體，允許前端連線
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 允許 React 開發伺服器
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含 API 路由
app.include_router(bot_control.router, prefix="/bot", tags=["Bot Control"])

# 包含 WebSocket 路由
@app.websocket("/ws/logs")
async def logs_websocket(websocket):
    await websocket_endpoint(websocket)