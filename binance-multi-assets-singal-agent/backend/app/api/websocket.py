from fastapi import WebSocket, WebSocketDisconnect
from typing import List

class LogBroadcaster:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)

log_broadcaster = LogBroadcaster()

async def websocket_endpoint(websocket: WebSocket):
    await log_broadcaster.connect(websocket)
    try:
        while True:
            # 保持連線開啟
            await websocket.receive_text()
    except WebSocketDisconnect:
        log_broadcaster.disconnect(websocket)