### ⚠️ 注意 / Caution — 請先確認存取權與用途 (請閱讀下面方法說明再執行) ⚠️
### ⚠️ Please confirm access rights and purpose first (please read the instructions below before proceeding). ⚠️
# How to download each folder only / 只下載單一資料夾

> If you only need a single folder from this monorepo (for example `amc-amr-gff-nn`) there are several simple ways to do that without downloading the entire repository.

> 若你只需要 monorepo 中的某個子資料夾（例如 `amc-amr-gff-nn`），以下是幾種方便的方法，可避免下載整個 repository。

### 1) Recommended — Git sparse-checkout (keep git history & branches)
- Best when you want to use git but only fetch the folder you need.
- Requires Git (recommended >= 2.25, update to latest if possible).

Bash / PowerShell:
```bash
# Clone with minimal blobs and enable sparse mode, then set the folder to fetch
git clone --filter=blob:none --sparse https://github.com/sinwulok/public-demos.git
cd public-demos

# Fetch only the folder you need (example)
git sparse-checkout set amc-amr-gff-nn

# Optionally checkout another branch:
git checkout <branch>   # replace <branch> with main/master or any branch name
```

若只要最新檔案且不需要歷史，可加 `--depth 1` 到 clone 指令。

### 2) Simple (no git) — SVN export (quick, no .git)
- Works for public GitHub repos and returns a plain folder without .git.
```bash
svn export https://github.com/sinwulok/public-demos/trunk/amc-amr-gff-nn
```
Note: the URL maps the repo default branch to `trunk`. For private repos you need SVN credentials.

### 3) Quick but heavy — Download ZIP and extract the folder
- Downloads the whole repository snapshot (larger), then extract only the folder you need.
```bash
curl -L -o repo.zip https://github.com/sinwulok/public-demos/archive/refs/heads/<branch>.zip
unzip repo.zip "public-demos-<branch>/amc-amr-gff-nn/*" -d extracted
```
Replace `<branch>` (e.g., `main`) as needed.

### 4) GitHub CLI helper (uses git clone flags)
If you use `gh`:
```bash
gh repo clone sinwulok/public-demos -- --filter=blob:none --sparse
cd public-demos
git sparse-checkout set amc-amr-gff-nn
```

### Notes / 注意事項
- For private repositories: use SSH (`git@github.com:owner/repo.git`) or HTTPS with credentials / PAT, or have users `gh auth login` first.
- `svn export` is convenient for public repos; private repos require authentication.
- Replace branch names (`<branch>`) with the branch you want (e.g., `main` or `master`).
- If users need full git history, do not use `--depth 1` and omit `--filter=blob:none`.
- Recommend showing the sparse-checkout method as the primary option for contributors who still want git capabilities.


# public-demos

A collection of public demos, notebooks, templates, and experimental projects across multiple domains.

This repository acts as a lightweight monorepo for standalone demos. Each top-level folder is an independent project with its own purpose, stack, and documentation.

<!-- START_PROJECT_OVERVIEW -->

## 專案總覽 | Project Overview

| Path | 類型 | 簡介 |
| --- | --- | --- |
| `animated-gradient-text-starter` | Frontend / UI Demo | Animated gradient text starter project built with Next.js, TypeScript, and Tailwind CSS. |
| `binance-multi-assets-singal-agent` | Quant / Trading | Multi-asset Binance trading signal agent / bot prototype with backend and frontend structure. |
| `bond-weighted-forecast` | Data Science / Forecasting | Forecasting / modeling demo related to weighted bond prediction. |
| `e-learning-fa-ipy` | Data Science / Machine Learning | E-learning data analysis project using Jupyter notebooks, with preprocessing, modeling, and visualization. |
| `machine-learning-applications-in-fmri` | Data Science / Research | Machine learning experiment or research demo focused on fMRI applications. |
| `r3f-portfolio` | Frontend / Portfolio | React Three Fiber portfolio with 3D visuals, animations, and interactive sections. |
| `sw-single-page-cv-latex-templates` | Templates / Utilities | LaTeX templates for single-page CV / resume documents. |

## Repository Structure

```text
.
├── .github/
├── animated-gradient-text-starter/
├── binance-multi-assets-singal-agent/
├── bond-weighted-forecast/
├── e-learning-fa-ipy/
├── machine-learning-applications-in-fmri/
├── r3f-portfolio/
└── sw-single-page-cv-latex-templates/
```

<!-- END_PROJECT_OVERVIEW -->

---

