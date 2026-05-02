from __future__ import annotations

import logging

from ..models import AssetState, RuntimeConfig
from ..types import BinanceClientProtocol


LOGGER = logging.getLogger(__name__)


def submit_order(client: BinanceClientProtocol, asset_state: AssetState, config: RuntimeConfig, side: str) -> None:
    symbol = asset_state.symbol(config.quote_asset)

    if not config.live_trading:
        LOGGER.info("DRY RUN %s %s %s", side, asset_state.order_size, symbol)
        return

    if side == "BUY":
        order = client.order_market_buy(symbol=symbol, quantity=asset_state.order_size)
    else:
        order = client.order_market_sell(symbol=symbol, quantity=asset_state.order_size)

    LOGGER.info("Submitted %s order for %s: %s", side, symbol, order)