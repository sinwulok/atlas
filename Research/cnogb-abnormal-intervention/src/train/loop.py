from typing import Any
import torch


def train_epoch(model: torch.nn.Module, loader, criterion, optimizer, device: str = "cpu") -> float:
    model.train()
    total_loss = 0.0
    count = 0
    for x, y in loader:
        x = x.to(device)
        y = y.to(device)
        optimizer.zero_grad()
        pred = model(x)
        loss = criterion(pred, y.squeeze(-1))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        count += 1
    return total_loss / max(1, count)


def evaluate_model_simple(model: torch.nn.Module, loader, criterion, device: str = "cpu") -> float:
    model.eval()
    total_loss = 0.0
    count = 0
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            y = y.to(device)
            pred = model(x)
            loss = criterion(pred, y.squeeze(-1))
            total_loss += loss.item()
            count += 1
    return total_loss / max(1, count)
