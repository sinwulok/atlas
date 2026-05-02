from __future__ import annotations

import logging
import time

from ..execution import submit_order
from ..market import get_bars
from ..models import AssetState, RuntimeConfig, StrategyDecision
from ..signals import add_indicators, evaluate_latest_signal
from ..types import BinanceClientProtocol


LOGGER = logging.getLogger(__name__)


def run_bot(client: BinanceClientProtocol, assets: list[AssetState], config: RuntimeConfig) -> None:
    iteration = 0

    while config.iterations == 0 or iteration < config.iterations:
        iteration += 1
        LOGGER.info("Starting iteration %s", iteration)

        for asset_state in assets:
            execute_trade_cycle(client, asset_state, config)

        LOGGER.info("Completed iteration %s", iteration)

        if config.iterations and iteration >= config.iterations:
            break

        time.sleep(config.poll_seconds)


def execute_trade_cycle(client: BinanceClientProtocol, asset_state: AssetState, config: RuntimeConfig) -> StrategyDecision:
    symbol = asset_state.symbol(config.quote_asset)
    bars = get_bars(client, symbol=symbol, interval=config.interval, lookback=config.lookback)
    enriched_bars = add_indicators(bars)
    decision = evaluate_latest_signal(symbol, enriched_bars)

    LOGGER.info(
        "%s | is_long=%s | macd=%.6f | pct_change_30m=%.6f | buy=%s | sell=%s",
        symbol,
        asset_state.is_long,
        decision.macd,
        decision.pct_change_30m,
        decision.should_buy,
        decision.should_sell,
    )

    if not asset_state.is_long and decision.should_buy:
        submit_order(client, asset_state, config, side="BUY")
        asset_state.is_long = True
    elif asset_state.is_long and decision.should_sell:
        submit_order(client, asset_state, config, side="SELL")
        asset_state.is_long = False

    return decision