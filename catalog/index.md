# 專案 Catalog | Project Catalog

本 catalog 提供 `workspace-atlas` repository 中所有專案的完整列表與分類。  
This catalog provides a complete listing and classification of all projects in the `workspace-atlas` repository.

---

## 概述 | Overview

`workspace-atlas` 是一個經治理的專案生態系，包含研究型、開發型與其他類型的專案。所有專案依類別組織，並以一致的 metadata 追蹤管理。  
`workspace-atlas` is a curated repository ecosystem containing research projects, development applications, and other types of projects. All projects are organized by category and tracked with consistent metadata.

---

## 專案分類 | Project Categories

### Research/

研究型專案，包含資料科學、機器學習、預測模型與學術實驗性質的內容。  
Research projects including data science, machine learning, forecasting models, and academic or experimental work.

- **cnogb-abnormal-intervention** — 使用 Transformer 模型進行債券預測與異常偵測。Bond forecasting and anomaly detection using Transformer models.
- **cnpbb-abnormal-drift** — 使用 Transformer 模型進行債券預測與異常偵測。Bond forecasting and anomaly detection using Transformer models.
- **machine-learning-applications-in-fmri** — 功能性 MRI 資料的機器學習應用研究。Machine learning applications for fMRI analysis.
- **e-learning-fa-ipy** — 使用 Jupyter Notebook 進行電子學習資料分析。E-learning data analysis using Jupyter notebooks.

### Development/

開發型專案，包含前端應用、交易訊號偵測、神經網路與應用程式原型。  
Development projects including frontend applications, trading signal detection, neural networks, and application prototypes.

- **amc-amr-gff-nn** — AMC AMR Gated Fusion Former 自動調變識別神經網路。AMC AMR Gated Fusion Former neural network for automatic modulation recognition.
- **animated-gradient-text-starter** — 動態漸層文字動畫入門專案（Next.js + TypeScript + Tailwind CSS）。Animated gradient text starter project built with Next.js, TypeScript, and Tailwind CSS.
- **r3f-portfolio** — React Three Fiber 3D 互動式作品集網站。React Three Fiber 3D portfolio website.
- **binance-multi-assets-singal-agent** — Binance 多資產交易訊號代理程式原型。Binance multi-asset trading signal agent prototype.

### Other/

模板、工具與通用用途的其他專案。  
Templates, tools, and utilities for general-purpose use.

- **sw-single-page-cv-latex-templates** — 單頁 CV / 履歷的 LaTeX 模板。LaTeX templates for single-page CV and resume documents.

---

## 專案生命週期 | Project Lifecycle

本 repository 使用以下生命週期狀態標記專案（作為 metadata，非實體目錄）：  
This repository uses the following lifecycle statuses to mark projects (as metadata, not physical directories):

- **incubation**（孵化中）— 早期階段、實驗性質的專案。Early-stage, experimental projects.
- **stable**（穩定）— 已完成主要功能、可供使用的專案。Completed main features, ready for use.
- **archived**（已封存）— 不再維護但保留作為參考的專案。No longer maintained but preserved for reference.

目前所有專案均標記為 **stable** 狀態。  
All projects are currently marked as **stable**.

---

## 專案標籤 | Tags

專案依以下標籤分類。完整標籤定義請參閱 [catalog/tags.yml](tags.yml)。  
Projects are categorized by the following tags. For full tag definitions, see [catalog/tags.yml](tags.yml).

### 資料科學與研究 | Data Science & Research
- **machine-learning** — 機器學習專案。Machine learning projects.
- **deep-learning** — 深度學習與神經網路。Deep learning and neural networks.
- **forecasting** — 預測與預報模型。Forecasting and prediction models.
- **research** — 學術研究專案。Academic research projects.
- **transformer** — Transformer 模型。Transformer models.
- **anomaly** — 異常偵測。Anomaly detection.

### 領域專屬 | Domain-Specific
- **finance** — 金融相關專案。Finance-related projects.
- **fmri** — 功能性 MRI 專案。Functional MRI projects.
- **education** — 教育相關專案。Education-related projects.
- **trading** — 交易與金融市場。Trading and financial markets.
- **quant** — 量化金融。Quantitative finance.

### 技術棧 | Technology Stack
- **neural-network** — 神經網路架構。Neural network architectures.
- **frontend** — 前端開發。Frontend development.
- **nextjs** — Next.js 框架。Next.js framework.
- **typescript** — TypeScript 語言。TypeScript language.
- **react** — React 函式庫。React library.
- **three-fiber** — React Three Fiber（3D 繪圖）。React Three Fiber (3D graphics).
- **jupyter** — Jupyter Notebook。Jupyter notebooks.
- **latex** — LaTeX 排版。LaTeX typesetting.

### 專案類型 | Project Types
- **ui** — 使用者介面專案。User interface projects.
- **portfolio** — 作品集網站。Portfolio websites.
- **agent** — 智慧代理程式。Intelligent agents.
- **template** — 模板專案。Template projects.
- **cv** — CV / 履歷專案。CV/resume projects.
- **resume** — 履歷文件。Resume documents.

### 平台與專屬技術 | Platforms & Specialized
- **binance** — Binance 交易所。Binance exchange.
- **automatic-modulation-recognition** — 自動調變識別系統。Automatic modulation recognition systems.
- **gated-fusion-former** — Gated Fusion Former 架構。Gated Fusion Former architecture.

---

## 索引檔案 | Catalog Files

- [`projects.yml`](projects.yml) — 機器可讀的專案 metadata。Machine-readable project metadata.
- [`index.md`](index.md) — 本文件，人類可讀的專案 catalog。This file, human-readable project catalog.
- [`metadata.schema.yml`](metadata.schema.yml) — Metadata 欄位定義。Metadata field definitions.
- [`tags.yml`](tags.yml) — 標籤定義與說明。Tag definitions and descriptions.
- [`statuses.yml`](statuses.yml) — 生命週期狀態定義。Lifecycle status definitions.
