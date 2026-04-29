from __future__ import annotations

import numpy as np
from nilearn.decomposition import DictLearning

from src.types import DecompositionResult


def fit_dict_learning(
    func_filenames: list[str],
    *,
    n_components: int = 20,
    random_state: int = 0,
    mask_strategy: str = "template",
    memory: str = "nilearn_cache",
    memory_level: int = 2,
    verbose: int = 1,
    n_epochs: int = 1,
) -> DecompositionResult:
    model = DictLearning(
        n_components=n_components,
        memory=memory,
        memory_level=memory_level,
        verbose=verbose,
        random_state=random_state,
        n_epochs=n_epochs,
        mask_strategy=mask_strategy,
    )
    model.fit(func_filenames)
    return DecompositionResult(
        model=model,
        components_img=model.components_img_,
        model_name="dict_learning",
        n_components=n_components,
    )


def score_dict_learning(model: DictLearning, func_filenames: list[str]) -> np.ndarray:
    return np.asarray(model.score(func_filenames, per_component=True))