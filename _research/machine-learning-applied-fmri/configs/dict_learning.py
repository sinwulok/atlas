from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DictLearningConfig:
    n_components: int = 20
    random_state: int = 0
    mask_strategy: str = "template"
    memory: str = "nilearn_cache"
    memory_level: int = 2
    verbose: int = 1
    n_epochs: int = 1