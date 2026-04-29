from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from numpy.typing import NDArray


@dataclass(slots=True)
class DatasetBundle:
    func_filenames: list[str]
    confounds: list[Any] | None
    description: str
    n_subjects: int


@dataclass(slots=True)
class DecompositionResult:
    model: Any
    components_img: Any
    model_name: str
    n_components: int


@dataclass(slots=True)
class RegionExtractionResult:
    extractor: Any
    regions_img: Any
    regions_index: list[int]
    n_regions: int
    title: str


@dataclass(slots=True)
class ConnectivityResult:
    subject_timeseries: list[NDArray[np.float64]]
    subject_correlations: list[NDArray[np.float64]]
    mean_correlation: NDArray[np.float64]


@dataclass(slots=True)
class DictionaryConnectivityWorkflowResult:
    region_extraction: RegionExtractionResult
    connectivity: ConnectivityResult