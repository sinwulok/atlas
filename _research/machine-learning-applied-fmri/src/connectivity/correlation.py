from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from nilearn.connectome import ConnectivityMeasure

from src.types import ConnectivityResult


def compute_group_correlation(
    subject_timeseries: list[NDArray[np.float64]],
    *,
    kind: str = "correlation",
) -> ConnectivityResult:
    connectome_measure = ConnectivityMeasure(kind=kind)
    subject_correlations: list[NDArray[np.float64]] = []

    for timeseries in subject_timeseries:
        correlation = connectome_measure.fit_transform([timeseries])[0]
        subject_correlations.append(correlation)

    mean_correlation = np.mean(subject_correlations, axis=0)
    return ConnectivityResult(
        subject_timeseries=subject_timeseries,
        subject_correlations=subject_correlations,
        mean_correlation=mean_correlation,
    )