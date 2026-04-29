from __future__ import annotations

from nilearn import datasets

from src.types import DatasetBundle


def load_development_fmri_dataset(n_subjects: int = 30) -> DatasetBundle:
    rest_dataset = datasets.fetch_development_fmri(n_subjects=n_subjects)
    return DatasetBundle(
        func_filenames=list(rest_dataset.func),
        confounds=list(rest_dataset.confounds) if getattr(rest_dataset, "confounds", None) is not None else None,
        description="Nilearn development fMRI dataset",
        n_subjects=n_subjects,
    )