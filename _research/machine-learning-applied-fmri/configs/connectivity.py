from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RegionExtractionConfig:
    threshold: float = 0.5
    thresholding_strategy: str = "ratio_n_voxels"
    extractor: str = "local_regions"
    standardize: bool = True
    min_region_size: int = 1350


@dataclass(slots=True)
class ConnectivityConfig:
    kind: str = "correlation"
    edge_threshold: str = "90%"