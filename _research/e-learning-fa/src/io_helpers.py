"""Simple IO helpers used by the core package."""
from typing import Optional
import pandas as pd


def read_csv(path: str, **kwargs) -> pd.DataFrame:
    """Read CSV into a DataFrame (wrapper over pandas)."""
    return pd.read_csv(path, **kwargs)


def read_excel(path: str, sheet_name: Optional[str] = None, **kwargs) -> pd.DataFrame:
    """Read Excel file into a DataFrame."""
    return pd.read_excel(path, sheet_name=sheet_name, **kwargs)


def ensure_dataframe(obj) -> pd.DataFrame:
    """If `obj` is a DataFrame return it, if it's a path try to read CSV."""
    if isinstance(obj, pd.DataFrame):
        return obj
    if isinstance(obj, str):
        return read_csv(obj)
    raise ValueError("Unsupported input type for ensure_dataframe")
