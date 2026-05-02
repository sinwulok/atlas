from __future__ import annotations

import pandas as pd

from ..types import BinanceClientProtocol
from .constants import KLINE_COLUMNS
from .transformers import normalize_kline_frame


def get_bars(
    client: BinanceClientProtocol,
    symbol: str,
    interval: str = "1m",
    lookback: str = "1 hour ago UTC",
) -> pd.DataFrame:
    raw_bars = client.get_historical_klines(symbol, interval, start_str=lookback)
    frame = pd.DataFrame(raw_bars, columns=KLINE_COLUMNS)
    return normalize_kline_frame(frame)