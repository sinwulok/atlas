from __future__ import annotations

from ..models import AssetState


DEFAULT_ASSETS = [
    AssetState(asset="BTC", order_size=0.0025, is_long=False),
    AssetState(asset="LTC", order_size=100, is_long=False),
    AssetState(asset="TRX", order_size=1000, is_long=False),
    AssetState(asset="ETH", order_size=0.03, is_long=False),
    AssetState(asset="BNB", order_size=0.25, is_long=False),
    AssetState(asset="XRP", order_size=100, is_long=False),
]


def clone_default_assets() -> list[AssetState]:
    return [AssetState(**asset.__dict__) for asset in DEFAULT_ASSETS]