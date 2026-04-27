# Repository 架構說明 | Architecture

## 概述 | Overview

本 repository 採用簡潔的功能分類結構，將專案依性質分為 Research、Development 和 Other 三大類別。

## 目錄結構 | Directory Structure

```
workspace-atlas/
├── Research/              # Research projects
├── Development/           # Development projects
├── Other/                 # Other types of projects
├── catalog/               # Project index and metadata
├── docs/                  # Governance documentation
├── .github/               # GitHub configuration and workflows
└── README.md              # Main repository documentation
```

## 目錄用途 | Directory Purposes

### Research/
用於存放研究型專案，包含：
- 資料科學專案
- 機器學習實驗
- 預測模型研究
- 學術或實驗性質的專案

### Development/
用於存放開發型專案，包含：
- 前端應用程式
- 後端服務
- 完整的應用程式原型
- 工具與實用程式

### Other/
用於存放不屬於上述兩類的專案，包含：
- 模板
- 文件範例
- 其他輔助資源

### catalog/
機器可讀的專案索引與 metadata，包含：
- `projects.yml` - 專案 metadata
- `index.md` - 專案索引
- `metadata.schema.yml` - metadata 欄位定義
- `tags.yml` - 標籤定義
- `statuses.yml` - 生命週期狀態定義

### docs/
人類可讀的治理文件，包含：
- 架構說明
- 遷移計畫
- 命名規範
- 專案生命週期
- 治理政策
- 分支策略

## 設計原則 | Design Principles

1. **簡潔性** - 避免過度分層，維持扁平化結構
2. **清晰性** - 每個目錄的用途明確且易於理解
3. **可維護性** - 結構穩定，不頻繁變更
4. **可擴展性** - 可輕鬆新增專案而不需重組結構
