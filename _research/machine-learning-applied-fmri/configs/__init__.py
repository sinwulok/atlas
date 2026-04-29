"""Project configuration modules for machine-learning-applied-fmri."""

from .base import ProjectPaths
from .canica import CanICAConfig
from .connectivity import ConnectivityConfig, RegionExtractionConfig
from .dict_learning import DictLearningConfig

__all__ = [
    "CanICAConfig",
    "ConnectivityConfig",
    "DictLearningConfig",
    "ProjectPaths",
    "RegionExtractionConfig",
]