"""Processing utilities for E-Learning factor analysis core.

Functions are small, well-documented, and accept DataFrame inputs so they
can be reused in other scripts or tests.
"""
from typing import Dict, Optional, Sequence, Tuple
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, FactorAnalyzer

DEFAULT_MAPPING: Dict[str, float] = {
    "Very Pos": 3.0,
    "Very Neg": -3.0,
    "Medium Pos": 2.0,
    "Medium Neg": -2.0,
    "Pos": 1.0,
    "Neg": -1.0,
}


def convert_responses(df: pd.DataFrame, mapping: Optional[Dict[str, float]] = None) -> pd.DataFrame:
    """Replace string responses with numeric scores and fill missing values.

    Returns a float DataFrame suitable for PCA/FA.
    """
    mapping = mapping or DEFAULT_MAPPING
    out = df.replace(mapping)
    # attempt numeric conversion where possible
    out = out.apply(pd.to_numeric, errors="coerce")
    out = out.fillna(0.0).astype(float)
    return out


def compute_bartlett(df: pd.DataFrame) -> Tuple[float, float]:
    """Run Bartlett's test of sphericity on the DataFrame.

    Returns (chi_square_value, p_value).
    """
    chi2, p = calculate_bartlett_sphericity(df)
    return chi2, p


def run_pca(df: pd.DataFrame, n_components: int = 4) -> Tuple[PCA, np.ndarray]:
    """Fit PCA and return fitted PCA object and transformed values."""
    pca = PCA(n_components=n_components)
    vals = pca.fit_transform(df)
    return pca, vals


def run_fa(df: pd.DataFrame, n_factors: int = 3, rotation: Optional[str] = "varimax") -> FactorAnalyzer:
    """Fit FactorAnalyzer and return the fitted object.

    The caller can then inspect `fa.loadings_`, `fa.get_communalities()`, etc.
    """
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation)
    fa.fit(df)
    return fa


def communalities(fa: FactorAnalyzer) -> pd.Series:
    """Return communalities as a pandas Series."""
    comm = fa.get_communalities()
    return pd.Series(comm)


def loadings_df(fa: FactorAnalyzer, columns: Sequence[str]) -> pd.DataFrame:
    """Return factor loadings as a DataFrame with given column names."""
    loadings = fa.loadings_
    names = [f"FA{i+1}" for i in range(loadings.shape[1])]
    return pd.DataFrame(loadings, columns=names, index=list(columns))
