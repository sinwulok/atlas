from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ProjectPaths:
    project_root: Path = Path(__file__).resolve().parents[1]
    assets_dir: Path = project_root / "assets"
    outputs_dir: Path = project_root / "outputs"
    cache_dir: Path = project_root / "nilearn_cache"

    def ensure_dirs(self) -> None:
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        self.outputs_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)