from __future__ import annotations

from src.connectivity.correlation import compute_group_correlation
from src.connectivity.timeseries import extract_subject_timeseries
from src.regions.extractor import extract_regions
from src.types import DatasetBundle, DecompositionResult, DictionaryConnectivityWorkflowResult


def run_dictionary_connectivity_pipeline(
    *,
    dataset: DatasetBundle,
    decomposition_result: DecompositionResult,
) -> DictionaryConnectivityWorkflowResult:
    region_result = extract_regions(
        decomposition_result.components_img,
        source_components=decomposition_result.n_components,
    )
    subject_timeseries = extract_subject_timeseries(
        dataset.func_filenames,
        dataset.confounds,
        region_result.extractor,
    )
    connectivity_result = compute_group_correlation(subject_timeseries)
    return DictionaryConnectivityWorkflowResult(
        region_extraction=region_result,
        connectivity=connectivity_result,
    )