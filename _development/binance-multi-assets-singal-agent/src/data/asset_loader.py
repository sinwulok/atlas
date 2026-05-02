from __future__ import annotations

from pathlib import Path

from ..models import AssetState
from .asset_sources import read_asset_rows
from .default_assets import DEFAULT_ASSETS, clone_default_assets


def load_assets(assets_file: Path | None) -> list[AssetState]:
    if assets_file is None or not assets_file.exists() or assets_file.stat().st_size == 0:
        return clone_default_assets()

    rows = read_asset_rows(assets_file)
    if not rows:
        return clone_default_assets()

    defaults = {asset.asset: asset for asset in DEFAULT_ASSETS}
    assets = [_build_asset_state(row, defaults) for row in rows]
    assets = [asset for asset in assets if asset is not None]
    return assets or clone_default_assets()


def _build_asset_state(row: dict[str, str], defaults: dict[str, AssetState]) -> AssetState | None:
    asset_name = (row.get("asset") or row.get("symbol") or "").strip().upper()
    if not asset_name:
        return None

    default_asset = defaults.get(asset_name, AssetState(asset=asset_name, order_size=1.0))
    order_size = _parse_order_size(row.get("order_size"), default_asset.order_size)
    is_long = _parse_is_long(row.get("is_long"), default_asset.is_long)
    return AssetState(asset=asset_name, order_size=order_size, is_long=is_long)


def _parse_order_size(raw_value: str | None, default_value: float) -> float:
    if raw_value is None or not str(raw_value).strip():
        return default_value
    return float(raw_value)


def _parse_is_long(raw_value: str | None, default_value: bool) -> bool:
    if raw_value is None or not str(raw_value).strip():
        return default_value
    return str(raw_value).strip().lower() in {"1", "true", "yes"}