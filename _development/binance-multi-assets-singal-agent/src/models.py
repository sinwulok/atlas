from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AssetState:
    asset: str
    order_size: float
    is_long: bool = False

    def symbol(self, quote_asset: str) -> str:
        return f"{self.asset.upper()}{quote_asset.upper()}"


@dataclass(frozen=True)
class StrategyDecision:
    symbol: str
    macd: float
    pct_change_30m: float
    should_buy: bool
    should_sell: bool


@dataclass(frozen=True)
class RuntimeConfig:
    api_key: str
    api_secret: str
    testnet: bool
    live_trading: bool
    quote_asset: str
    interval: str
    lookback: str
    poll_seconds: int
    iterations: int