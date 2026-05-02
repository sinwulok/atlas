from __future__ import annotations

from typing import Any, Protocol


class BinanceClientProtocol(Protocol):
    def get_historical_klines(self, symbol: str, interval: str, start_str: str) -> list[list[Any]]: ...

    def order_market_buy(self, symbol: str, quantity: float) -> Any: ...

    def order_market_sell(self, symbol: str, quantity: float) -> Any: ...