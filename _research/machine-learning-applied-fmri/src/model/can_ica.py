from __future__ import annotations

from nilearn.decomposition import CanICA

from src.types import DecompositionResult


def fit_canica(
    func_filenames: list[str],
    *,
    n_components: int = 20,
    random_state: int = 0,
    mask_strategy: str = "template",
    memory: str = "nilearn_cache",
    memory_level: int = 2,
    verbose: int = 10,
) -> DecompositionResult:
    model = CanICA(
        n_components=n_components,
        memory=memory,
        memory_level=memory_level,
        verbose=verbose,
        mask_strategy=mask_strategy,
        random_state=random_state,
    )
    model.fit(func_filenames)
    return DecompositionResult(
        model=model,
        components_img=model.components_img_,
        model_name="canica",
        n_components=n_components,
    )