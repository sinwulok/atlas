from __future__ import annotations

import pandas as pd
import pandas_ta as ta


def get_macd(data: pd.Series, slow: int = 26, fast: int = 12, signal: int = 9) -> pd.Series:
    macd_frame = ta.macd(data, slow=slow, fast=fast, signal=signal)
    if macd_frame is None or macd_frame.empty:
        raise ValueError("Unable to calculate MACD for the provided data.")
    return macd_frame.iloc[:, -1]


def add_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame

    enriched = frame.copy()
    enriched["MACD"] = get_macd(enriched["Close"])
    enriched["Pct Change 30m"] = enriched["Close"].pct_change(30)
    return enriched.dropna()