from __future__ import annotations

import pandas as pd

from ..models import StrategyDecision


def evaluate_latest_signal(symbol: str, frame: pd.DataFrame) -> StrategyDecision:
    if frame.empty:
        raise ValueError(f"No market data available for {symbol}.")

    latest = frame.iloc[-1]
    macd = float(latest["MACD"])
    pct_change_30m = float(latest["Pct Change 30m"])
    should_buy = macd > 0 and pct_change_30m > 0
    should_sell = macd < 0 and pct_change_30m < 0
    return StrategyDecision(
        symbol=symbol,
        macd=macd,
        pct_change_30m=pct_change_30m,
        should_buy=should_buy,
        should_sell=should_sell,
    )