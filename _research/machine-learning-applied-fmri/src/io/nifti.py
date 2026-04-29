from __future__ import annotations

from typing import Any


def save_nifti_image(image: Any, output_path: str) -> None:
    image.to_filename(output_path)