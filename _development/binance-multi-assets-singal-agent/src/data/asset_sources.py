from __future__ import annotations

import csv
from pathlib import Path


def read_asset_rows(assets_file: Path) -> list[dict[str, str]]:
    if assets_file.suffix.lower() == ".csv":
        return _read_asset_rows_from_csv(assets_file)
    return _read_asset_rows_from_txt(assets_file)


def _read_asset_rows_from_csv(assets_file: Path) -> list[dict[str, str]]:
    with assets_file.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_asset_rows_from_txt(assets_file: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for raw_line in assets_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [part.strip() for part in line.split(",")]
        rows.append(
            {
                "asset": parts[0] if len(parts) > 0 else "",
                "order_size": parts[1] if len(parts) > 1 else "",
                "is_long": parts[2] if len(parts) > 2 else "",
            }
        )

    return rows