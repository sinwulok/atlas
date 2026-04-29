"""CLI entrypoint for the machine-learning-applied-fmri pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from configs.base import ProjectPaths
from src.data.loader import load_development_fmri_dataset
from src.io import save_nifti_image, save_numpy_array
from src.pipeline.connectome import run_dictionary_connectivity_pipeline
from src.pipeline.decompose import run_decomposition_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the fMRI analysis pipeline.")
    parser.add_argument("--n-subjects", type=int, default=30, help="Number of subjects to fetch")
    parser.add_argument("--n-components", type=int, default=20, help="Number of decomposition components")
    parser.add_argument(
        "--model",
        choices=("canica", "dict", "both"),
        default="both",
        help="Which decomposition pipeline to run",
    )
    parser.add_argument(
        "--connectivity",
        action="store_true",
        help="Run region extraction and group connectivity from dictionary learning results",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional output directory for saving derived artifacts",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = ProjectPaths()
    paths.ensure_dirs()
    dataset = load_development_fmri_dataset(n_subjects=args.n_subjects)
    output_dir = args.output_dir or paths.outputs_dir / "cli"

    if args.model in {"canica", "both"}:
        canica_result = run_decomposition_pipeline(
            dataset=dataset,
            model_name="canica",
            n_components=args.n_components,
        )
        print(f"CanICA fitted with {canica_result.n_components} components")
        save_nifti_image(canica_result.components_img, output_dir / "canica_components.nii.gz")

    if args.model in {"dict", "both"}:
        dict_result = run_decomposition_pipeline(
            dataset=dataset,
            model_name="dict_learning",
            n_components=args.n_components,
        )
        print(f"DictLearning fitted with {dict_result.n_components} components")
        save_nifti_image(dict_result.components_img, output_dir / "dict_learning_components.nii.gz")

        if args.connectivity:
            workflow_result = run_dictionary_connectivity_pipeline(dataset=dataset, decomposition_result=dict_result)
            save_nifti_image(
                workflow_result.region_extraction.regions_img,
                output_dir / "dict_learning_regions.nii.gz",
            )
            save_numpy_array(
                workflow_result.connectivity.mean_correlation,
                output_dir / "mean_correlation.npy",
            )
            print(
                "Computed mean correlation matrix with shape "
                f"{workflow_result.connectivity.mean_correlation.shape}"
            )


if __name__ == "__main__":
    main()