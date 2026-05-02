from __future__ import annotations

import pandas as pd

from .constants import PRICE_COLUMNS


def normalize_kline_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame

    normalized = frame.copy()
    normalized["Open time"] = pd.to_datetime(normalized["Open time"], unit="ms")
    normalized.set_index("Open time", inplace=True)
    normalized = normalized.loc[:, PRICE_COLUMNS]

    for column in normalized.columns:
        normalized[column] = pd.to_numeric(normalized[column], errors="coerce")

    return normalized.dropna()