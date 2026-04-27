import numpy as np
import torch
from typing import Tuple


def predict_with_mc_dropout(model: torch.nn.Module, loader, device: str = "cpu", n_samples: int = 20) -> Tuple[np.ndarray, np.ndarray]:
    model.train()  # enable dropout
    all_preds = []
    with torch.no_grad():
        for _ in range(n_samples):
            preds = []
            for x, _ in loader:
                x = x.to(device)
                p = model(x).cpu().numpy()
                preds.append(p)
            all_preds.append(np.concatenate(preds, axis=0))
    all_preds = np.stack(all_preds, axis=0)
    mean = np.mean(all_preds, axis=0)
    std = np.std(all_preds, axis=0)
    return mean, std
