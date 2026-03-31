#!/usr/bin/env python3
"""

- 列出 repo 根目錄的一層子資料夾。
- 讀取 root/catalog.yml (若存在) 並以其為優先資料來源。
- 若 catalog 無 type/description，嘗試讀取該子資料夾的 README.md:
  1) 先讀 YAML front-matter (若有)
  2) 否則擷取第一個有意義段落作為 summary
- 產生兩個區塊（Project Overview table 與 Repository Structure）並替換 README.md 中
  <!-- START_PROJECT_OVERVIEW --> 與 <!-- END_PROJECT_OVERVIEW --> 之間的內容。
"""
from pathlib import Path
import os
import re
import yaml
from textwrap import shorten

ROOT = Path(os.getenv("GITHUB_WORKSPACE", "." )).resolve()
README_PATH = ROOT / "README.md"
CATALOG_PATH = ROOT / "catalog.yml"

EXCLUDE = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', 'outputs'}
MARKER_START = "<!-- START_PROJECT_OVERVIEW -->"
MARKER_END = "<!-- END_PROJECT_OVERVIEW -->"

def load_catalog():
    if not CATALOG_PATH.exists():
        return {}
    try:
        data = yaml.safe_load(CATALOG_PATH.read_text(encoding='utf-8'))
        return data.get("projects", {}) if isinstance(data, dict) else {}
    except Exception as e:
        print(f"Warning: failed to load catalog.yml: {e}")
        return {}

def list_top_dirs(root: Path):
    items = []
    for p in sorted(root.iterdir()):
        if p.name in EXCLUDE:
            continue
        if p.is_dir():
            items.append(p.name)
    return items

def read_front_matter(text: str):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}

def extract_summary_from_readme(text: str):
    # remove front matter if present
    text = re.sub(r"^---(.|\n)*?---\s*\n", "", text)
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    for p in parts:
        if p.startswith('#') or p.startswith('![') or len(p) < 10:
            continue
        single = ' '.join(line.strip() for line in p.splitlines())
        return shorten(single, width=200, placeholder='...')
    return ""

def safe_escape_md(text: str) -> str:
    if text is None:
        return ""
    return text.replace("|", "\\|").replace("\n", " ").strip()

def build_overview_table(entries):
    # entries: list of (path, type, desc)
    header = "## 專案總覽 | Project Overview\n\n"
    header += "| Path | 類型 | 簡介 |\n| --- | --- | --- |\n"
    rows = []
    for path, type_, desc in entries:
        type_ = type_ or ""
        desc = safe_escape_md(desc or "")
        rows.append(f"| `{path}` | {type_} | {desc} |")
    return header + "\n".join(rows) + "\n"

def build_repository_structure(dirs):
    lines = [ "## Repository Structure\n", "```text", ".", ]
    n = len(dirs)
    for i, d in enumerate(dirs):
        prefix = "└── " if i == n-1 else "├── "
        lines.append(f"{prefix}{d}/")
    lines.append("```")
    return "\n".join(lines) + "\n"

def main():
    catalog = load_catalog()
    dirs = list_top_dirs(ROOT)

    entries = []
    for d in dirs:
        cat_entry = catalog.get(d, {}) if isinstance(catalog, dict) else {}
        if isinstance(cat_entry, dict) and cat_entry.get("exclude"):
            # skip this folder entirely
            continue

        type_ = cat_entry.get("type") if isinstance(cat_entry, dict) else None
        desc = cat_entry.get("description") if isinstance(cat_entry, dict) else None

        if not (type_ and desc):
            readme_file = ROOT / d / "README.md"
            if readme_file.exists():
                try:
                    txt = readme_file.read_text(encoding="utf-8", errors="ignore")
                    fm = read_front_matter(txt)
                    if not type_:
                        type_ = fm.get("type")
                    if not desc:
                        desc = fm.get("description") or extract_summary_from_readme(txt)
                except Exception as e:
                    print(f"Warning: failed to read {readme_file}: {e}")

        entries.append((d, type_ or "", desc or ""))

    table_md = build_overview_table(entries)
    tree_md = build_repository_structure([e[0] for e in entries])

    combined = table_md + "\n" + tree_md

    if README_PATH.exists():
        readme_text = README_PATH.read_text(encoding="utf-8", errors="ignore")
    else:
        readme_text = ""

    if MARKER_START in readme_text and MARKER_END in readme_text:
        before, rest = readme_text.split(MARKER_START, 1)
        _, after = rest.split(MARKER_END, 1)
        new_readme = before + MARKER_START + "\n\n" + combined + "\n" + MARKER_END + after
    else:
        # 在檔尾加入標記區塊
        if readme_text and not readme_text.endswith("\n"):
            readme_text += "\n"
        new_readme = readme_text + MARKER_START + "\n\n" + combined + "\n" + MARKER_END + "\n"

    if new_readme != readme_text:
        README_PATH.write_text(new_readme, encoding="utf-8")
        print("README.md updated with project overview and repository structure.")
    else:
        print("No changes to README.md")

if __name__ == "__main__":
    main()
