# Repository 治理政策 | Governance

## 目標 | Goals

本 repository 的治理目標為：

1. **組織性** - 維持清晰的專案結構與分類
2. **可存取性** - 讓使用者能輕鬆找到並使用專案
3. **可維護性** - 確保 repository 長期可維護
4. **一致性** - 建立並遵循統一的規範與慣例

## 專案管理 | Project Management

### 新增專案

1. 確定專案類別（`research/` / `development/` / `other/`）
2. 在對應目錄下建立專案資料夾
3. 更新 `catalog/projects.yml` 新增專案 metadata
4. 在專案內建立基本 README

### 移除專案

1. 將專案 lifecycle 設為 `archived`
2. 在專案 README 中說明封存原因
3. 保留專案在 `catalog/projects.yml` 中的記錄

### 重新分類專案

1. 移動專案到新的類別目錄
2. 更新 `catalog/projects.yml` 中的 `path` 和 `category`
3. 更新相關文件

## 文件管理 | Documentation Management

### 必要文件

- `README.md` - Repository 根目錄說明
- `catalog/projects.yml` - 專案索引
- `catalog/index.md` - 專案目錄
- `docs/*.md` - 治理文件

### 文件更新

- 新增或移除專案時更新索引
- 架構變更時更新文件
- 定期檢查文件的準確性

## 分支策略 | Branch Strategy

請參閱 `docs/branch-policy.md`。

## 權限管理 | Permission Management

（根據實際需求補充）

## 標準與規範 | Standards and Conventions

- **命名規範** - 參閱 `docs/naming-conventions.md`
- **專案生命週期** - 參閱 `docs/project-lifecycle.md`
- **架構設計** - 參閱 `docs/architecture.md`
