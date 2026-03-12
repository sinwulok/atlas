from fastapi import APIRouter
from app.services.trading_bot import trading_bot_instance

router = APIRouter()

@router.post("/start")
async def start_bot():
    return trading_bot_instance.start()

@router.post("/stop")
async def stop_bot():
    return trading_bot_instance.stop()

@router.get("/status")
async def get_bot_status():
    return trading_bot_instance.get_status()