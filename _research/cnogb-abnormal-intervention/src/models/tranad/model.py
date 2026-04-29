"""Initial scaffold for TranAD-style experiments."""

from dataclasses import dataclass
from typing import Optional

from src.models._shared import BackboneConfig, build_backbone_model


@dataclass
class TranADConfig(BackboneConfig):
    adversarial_weight: float = 1.0


def build_tranad(feature_dim: int, config: Optional[TranADConfig] = None, device: Optional[str] = None):
    return build_backbone_model(feature_dim, config or TranADConfig(num_layers=3), device)


__all__ = ["TranADConfig", "build_tranad"]
