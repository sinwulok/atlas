"""Run the group ICA plus dictionary learning workflow and save outputs to disk."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.base import ProjectPaths
from src.data.loader import load_development_fmri_dataset
from src.io import (
    save_display_figure,
    save_html_view,
    save_matplotlib_figure,
    save_nifti_image,
    save_numpy_array,
)
from src.model.dict_learn import score_dict_learning
from src.pipeline.connectome import run_dictionary_connectivity_pipeline
from src.pipeline.decompose import run_decomposition_pipeline
from src.plot.components import plot_component_atlas, plot_component_maps
from src.plot.connectivity import (
    find_connectome_coords,
    plot_connectivity_matrix,
    plot_connectome_view,
    view_connectome,
)
from src.plot.regions import plot_region_atlas
from src.plot.scores import plot_component_scores


def main() -> None:
    paths = ProjectPaths()
    paths.ensure_dirs()
    output_dir = paths.outputs_dir / "group_ica_dictlearn"
    output_dir.mkdir(parents=True, exist_ok=True)

    dataset = load_development_fmri_dataset(n_subjects=30)
    canica_result = run_decomposition_pipeline(dataset=dataset, model_name="canica", n_components=20)
    dict_result = run_decomposition_pipeline(dataset=dataset, model_name="dict_learning", n_components=20)
    workflow_result = run_dictionary_connectivity_pipeline(dataset=dataset, decomposition_result=dict_result)

    save_nifti_image(canica_result.components_img, output_dir / "canica_components.nii.gz")
    save_nifti_image(dict_result.components_img, output_dir / "dict_learning_components.nii.gz")
    save_nifti_image(workflow_result.region_extraction.regions_img, output_dir / "regions_extracted.nii.gz")
    save_numpy_array(workflow_result.connectivity.mean_correlation, output_dir / "mean_correlation.npy")

    canica_atlas = plot_component_atlas(canica_result.components_img, title="All ICA components")
    save_display_figure(canica_atlas, output_dir / "canica_components.png")

    dict_atlas = plot_component_atlas(dict_result.components_img, title="All DictLearning components")
    save_display_figure(dict_atlas, output_dir / "dict_learning_components.png")

    region_atlas = plot_region_atlas(
        workflow_result.region_extraction.regions_img,
        title=workflow_result.region_extraction.title,
    )
    save_display_figure(region_atlas, output_dir / "regions_extracted.png")

    score_figure, _ = plot_component_scores(score_dict_learning(dict_result.model, dataset.func_filenames))
    save_matplotlib_figure(score_figure, output_dir / "dict_learning_scores.png")

    matrix_title = f"Correlation between {workflow_result.region_extraction.n_regions} regions"
    matrix_display = plot_connectivity_matrix(workflow_result.connectivity.mean_correlation, title=matrix_title)
    save_display_figure(matrix_display, output_dir / "connectivity_matrix.png")

    coords_connectome = find_connectome_coords(workflow_result.region_extraction.regions_img)
    connectome_display = plot_connectome_view(
        workflow_result.connectivity.mean_correlation,
        coords_connectome,
        title=matrix_title,
    )
    save_display_figure(connectome_display, output_dir / "connectome.png")

    connectome_view = view_connectome(
        workflow_result.connectivity.mean_correlation,
        coords_connectome,
        title=matrix_title,
    )
    save_html_view(connectome_view, output_dir / "connectome.html")

    # Save a small sample of per-component stat maps for quick inspection.
    component_displays = plot_component_maps(dict_result.components_img, title_prefix="Comp")
    for index, display in enumerate(component_displays[:3]):
        save_display_figure(display, output_dir / f"dict_component_{index:02d}.png")


if __name__ == "__main__":
    main()