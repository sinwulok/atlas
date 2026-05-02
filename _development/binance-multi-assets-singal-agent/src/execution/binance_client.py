from __future__ import annotations

from ..types import BinanceClientProtocol


def create_client(api_key: str, api_secret: str, testnet: bool) -> BinanceClientProtocol:
    from binance.client import Client

    return Client(api_key or "", api_secret or "", testnet=testnet)


def validate_credentials(api_key: str, api_secret: str, live_trading: bool) -> None:
    if live_trading and (not api_key or not api_secret):
        raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET are required for live trading.")