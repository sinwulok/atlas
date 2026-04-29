from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def plot_component_scores(scores: np.ndarray):
    figure, axis = plt.subplots(figsize=(4, 4))
    positions = np.arange(len(scores))
    axis.barh(positions, scores)
    axis.set_ylabel("Component #", size=12)
    axis.set_xlabel("Explained variance", size=12)
    axis.set_yticks(np.arange(len(scores)))
    axis.xaxis.set_major_formatter(FormatStrFormatter("%.3f"))
    figure.tight_layout()
    return figure, axis