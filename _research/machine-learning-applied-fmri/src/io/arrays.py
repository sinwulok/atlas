from __future__ import annotations

from pathlib import Path

import numpy as np
from numpy.typing import NDArray


def save_numpy_array(array: NDArray[np.float64], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, array)