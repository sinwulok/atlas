"""Pipeline orchestration helpers."""

from .connectome import run_dictionary_connectivity_pipeline
from .decompose import run_decomposition_pipeline

__all__ = ["run_decomposition_pipeline", "run_dictionary_connectivity_pipeline"]