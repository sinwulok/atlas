import numpy as np
from typing import Callable


def calculate_permutation_importance(predict_fn: Callable, X: np.ndarray, y: np.ndarray, metric_fn: Callable, n_repeats: int = 5):
    baseline = metric_fn(y, predict_fn(X))
    importances = []
    for col in range(X.shape[1]):
        scores = []
        X_perm = X.copy()
        for _ in range(n_repeats):
            col_vals = X_perm[:, col].copy()
            np.random.shuffle(col_vals)
            X_perm[:, col] = col_vals
            scores.append(metric_fn(y, predict_fn(X_perm)))
        importances.append(np.mean(scores) - baseline)
    return np.array(importances)
