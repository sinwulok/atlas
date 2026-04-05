# public-demos

A collection of public demos, notebooks, templates, and experimental projects across multiple domains.

本 repository 採用功能分類的治理結構，將專案依性質分為 Research、Development 和 Other 三大類別。

---

## 目錄結構 | Repository Structure

```
public-demos/
├── Research/              # 研究型專案
├── Development/           # 開發型專案
├── Other/                 # 其他類型專案
├── catalog/               # 專案索引與 metadata
├── docs/                  # 治理文件
├── .github/               # GitHub 設定與工作流程
└── README.md              # 本檔案
```

---

## 專案分類 | Project Categories

### Research/
研究型專案，包含資料科學、機器學習、預測模型等學術或實驗性質的專案。

- **ogb-bond-signal-anomaly** - 債券加權預測/建模示範（原 bond-weighted-forecast）
- **machine-learning-applications-in-fmri** - fMRI 機器學習應用研究
- **e-learning-fa-ipy** - 電子學習資料分析專案（使用 Jupyter notebooks）

### Development/
開發型專案，包含前端應用、交易機器人、神經網路等開發中或已完成的應用程式。

- **amc-amr-gff-nn** - AMC AMR GFF 神經網路專案
- **animated-gradient-text-starter** - 動態漸層文字啟動專案（Next.js + TypeScript + Tailwind）
- **r3f-portfolio** - React Three Fiber 3D 作品集網站
- **binance-multi-assets-singal-agent** - Binance 多資產交易訊號代理/機器人原型

### Other/
其他類型專案，包含模板、工具等非研究或開發性質的內容。

- **sw-single-page-cv-latex-templates** - LaTeX 單頁履歷模板

---

## 專案索引 | Project Catalog

完整的專案列表、metadata 與標籤資訊請參閱：
- **機器可讀**：[catalog/projects.yml](catalog/projects.yml)
- **人類可讀**：[catalog/index.md](catalog/index.md)

---

## 治理文件 | Governance

本 repository 的治理文件位於 `docs/` 目錄：

- [架構說明](docs/architecture.md) - Repository 架構與目錄用途
- [遷移計畫](docs/migration-plan.md) - 重構遷移的詳細記錄
- [命名規範](docs/naming-conventions.md) - 專案與檔案命名規範
- [專案生命週期](docs/project-lifecycle.md) - 專案狀態管理
- [治理政策](docs/governance.md) - Repository 治理原則
- [分支策略](docs/branch-policy.md) - 分支管理與開發流程

---

## 如何下載單一專案 | How to Download a Single Project

如果您只需要 monorepo 中的某個子資料夾，以下是幾種方便的方法，可避免下載整個 repository。

### 方法 1：Git sparse-checkout（推薦）

最適合需要使用 git 但只想取得特定資料夾的情況。

```bash
# Clone with minimal blobs and enable sparse mode
git clone --filter=blob:none --sparse https://github.com/sinwulok/public-demos.git
cd public-demos

# Fetch only the folder you need (example)
git sparse-checkout set Research/ogb-bond-signal-anomaly

# Optionally checkout another branch
git checkout <branch>
```

### 方法 2：SVN export（快速，無 git）

適合公開 GitHub repos，返回純資料夾，不含 .git。

```bash
svn export https://github.com/sinwulok/public-demos/trunk/Research/ogb-bond-signal-anomaly
```

### 方法 3：下載 ZIP 並解壓縮特定資料夾

下載整個 repository 的快照（較大），然後只解壓縮需要的資料夾。

```bash
curl -L -o repo.zip https://github.com/sinwulok/public-demos/archive/refs/heads/<branch>.zip
unzip repo.zip "public-demos-<branch>/Research/ogb-bond-signal-anomaly/*" -d extracted
```

將 `<branch>` 替換為分支名稱（例如 `main`）。

### 方法 4：GitHub CLI

如果使用 `gh` CLI：

```bash
gh repo clone sinwulok/public-demos -- --filter=blob:none --sparse
cd public-demos
git sparse-checkout set Research/ogb-bond-signal-anomaly
```

---

## 注意事項 | Notes

- 私有 repositories 需要使用 SSH 或 HTTPS 驗證
- `svn export` 適合公開 repos；私有 repos 需要認證
- 若需要完整 git 歷史，請勿使用 `--depth 1` 和 `--filter=blob:none`
- 建議優先使用 sparse-checkout 方法，適合需要 git 功能的貢獻者

---

## 貢獻 | Contributing

（根據實際需求補充貢獻指南）

---

## 授權 | License

（根據實際需求補充授權資訊）
