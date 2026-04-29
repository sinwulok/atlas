from __future__ import annotations

from pathlib import Path
from typing import Any


def save_display_figure(display: Any, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    display.savefig(str(path))


def save_matplotlib_figure(figure: Any, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path)


def save_html_view(view: Any, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    view.save_as_html(str(path))