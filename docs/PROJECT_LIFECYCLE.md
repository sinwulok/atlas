# 專案生命週期 | Project Lifecycle

## 概述 | Overview

專案生命週期用於標記專案的開發階段與維護狀態。生命週期狀態**不建立為實體目錄**，而是作為 metadata 儲存在 `catalog/projects.yml` 中。

## 生命週期階段 | Lifecycle Stages

### 1. Incubation（孵化中）

**定義：** 早期階段、實驗性質的專案。

**特徵：**
- 專案處於早期開發階段
- API 或架構可能隨時變更
- 尚未完成主要功能
- 適合實驗與探索

**適用情境：**
- 新專案剛開始開發
- 概念驗證（Proof of Concept）
- 技術探索與實驗

### 2. Stable（穩定）

**定義：** 已完成主要功能、可供使用的專案。

**特徵：**
- 主要功能已完成
- 可供使用或參考
- 架構相對穩定
- 有基本文件說明

**適用情境：**
- 專案已完成開發並可使用
- 具有穩定的 API 或介面
- 適合作為參考或基礎

### 3. Archived（已封存）

**定義：** 不再維護但保留作為參考的專案。

**特徵：**
- 不再進行主動開發
- 保留作為歷史參考
- 可能使用過時的技術或方法
- 建議參考其他替代專案

**適用情境：**
- 專案已完成其使命
- 技術棧已過時但保留參考價值
- 已有更好的替代方案

## 狀態轉換 | Status Transitions

```
Incubation → Stable → Archived
     ↓         ↓
  Archived  Archived
```

專案可以：
- 從 Incubation 發展到 Stable
- 從 Incubation 直接變為 Archived（如實驗失敗）
- 從 Stable 變為 Archived（如停止維護）

## 狀態管理 | Status Management

### 如何標記生命週期狀態

在 `catalog/projects.yml` 中設定 `lifecycle` 欄位：

```yaml
projects:
  project-name:
    path: Category/project-name
    lifecycle: stable  # incubation, stable, 或 archived
```

### 如何查詢專案狀態

查看 `catalog/projects.yml` 或 `catalog/index.md`。

## 目前狀態 | Current Status

目前所有專案均標記為 **stable** 狀態。
