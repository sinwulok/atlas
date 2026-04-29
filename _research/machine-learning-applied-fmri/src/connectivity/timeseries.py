from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray


def extract_subject_timeseries(
    func_filenames: list[str],
    confounds: list[Any] | None,
    extractor: Any,
) -> list[NDArray[np.float64]]:
    if confounds is None:
        confounds = [None] * len(func_filenames)

    subject_timeseries: list[NDArray[np.float64]] = []
    for filename, confound in zip(func_filenames, confounds):
        subject_timeseries.append(extractor.transform(filename, confounds=confound))
    return subject_timeseries