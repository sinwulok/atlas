# 分支策略 | Branch Policy

## 分支結構 | Branch Structure

本 repository 採用簡化的分支策略：

### 主要分支 | Main Branches

- **`main`** - 主分支，包含當前穩定的 repository 結構

### 特殊分支 | Special Branches

- **`archived/migration`** - 保存舊的 repository 結構，用於歷史參考

## 分支管理原則 | Branch Management Principles

### main 分支

- 用途：當前穩定版本的 repository
- 保護：建議設定分支保護規則
- 更新：透過 Pull Request 合併變更

### archived/migration 分支

- 用途：保存遷移前的舊結構
- 狀態：唯讀，不再更新
- 保留原因：歷史參考與回溯

## 開發流程 | Development Workflow

### 新增或修改專案

1. 從 `main` 建立功能分支
2. 進行變更
3. 提交 Pull Request
4. 審核後合併到 `main`

### 分支命名

功能分支建議使用以下格式：
- `feature/<description>` - 新功能
- `fix/<description>` - 修復
- `docs/<description>` - 文件更新
- `refactor/<description>` - 重構

範例：
- `feature/add-new-project`
- `docs/update-readme`
- `fix/correct-metadata`

## 不建立的分支 | Branches Not Created

本 repository **不建立**以下類型的長期分支：
- `develop`
- `staging`
- `incubation/*`（生命週期狀態不使用分支管理）
- `stable/*`（生命週期狀態不使用分支管理）

## Pull Request 政策 | Pull Request Policy

### PR 要求

- 標題清晰描述變更內容
- 說明變更原因與影響範圍
- 必要時更新相關文件
- 確保不破壞現有專案

### PR 審核

- 檢查是否符合命名規範
- 確認 metadata 更新正確
- 驗證文件同步更新

## 保護規則 | Protection Rules

建議為 `main` 分支設定以下保護規則：
- 要求 Pull Request 審核
- 禁止強制推送
- 要求分支為最新狀態
