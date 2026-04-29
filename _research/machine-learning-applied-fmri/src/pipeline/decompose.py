from __future__ import annotations

from src.model.can_ica import fit_canica
from src.model.dict_learn import fit_dict_learning
from src.types import DatasetBundle, DecompositionResult


def run_decomposition_pipeline(
    *,
    dataset: DatasetBundle,
    model_name: str,
    n_components: int = 20,
) -> DecompositionResult:
    if model_name == "canica":
        return fit_canica(dataset.func_filenames, n_components=n_components)
    if model_name == "dict_learning":
        return fit_dict_learning(dataset.func_filenames, n_components=n_components)
    raise ValueError(f"Unsupported model_name: {model_name}")