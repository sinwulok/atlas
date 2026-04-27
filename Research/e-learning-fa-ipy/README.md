# e-learning-fa-ipy

使用 Jupyter Notebook 進行電子學習資料分析，包含前處理、建模與視覺化。  
E-learning data analysis using Jupyter notebooks with preprocessing, modeling, and visualization.

---

## 概述 | Overview

本專案針對電子學習資料進行分析與探索，包含前處理、統計分析、建模與視覺化，主要使用 Jupyter Notebook 進行互動式分析。  
This project focuses on analyzing and exploring E-learning data, including preprocessing, statistical analysis, modeling, and visualization, primarily using Jupyter Notebook for interactive analysis.

---

## 類別與狀態 | Category and Lifecycle

- **類別 | Category**：Research
- **類型 | Type**：Machine Learning | Functional Component Analysis
- **生命週期 | Lifecycle**：stable
- **標籤 | Tags**：machine-learning, jupyter, education

---

## 結構 | Structure

```text
Research/e-learning-fa-ipy/
├── data/                   # 資料集（.sav 檔）| Datasets (.sav files)
├── notebooks/              # Jupyter Notebook 檔案 | Jupyter Notebook files
├── scripts/                # 可重用 Python 腳本 | Reusable Python scripts
├── results/                # 分析結果與視覺化 | Analysis results and visualizations
├── assets/                 # 結果圖片 | Result images
└── README.md               # 本文件 | This file
```

---

## 如何執行 | How to Run

1. 安裝相依套件 | Install dependencies:
   ```bash
   pip install pandas pyreadstat factor-analyzer scikit-learn matplotlib jupyter
   ```

2. 啟動 Jupyter Notebook | Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. 開啟並執行分析 Notebook。  
   Open and run the analysis notebooks.

4. 在 `results/` 與 `assets/` 目錄查看結果。  
   View results in the `results/` and `assets/` directories.

---

## 相依項目 | Dependencies

- pandas — 資料處理。Data manipulation.
- pyreadstat — 處理 .sav 檔案。Handling .sav files.
- factor_analyzer — 因素分析。Factor analysis.
- scikit-learn — 分解與建模。Decomposition & modeling.
- matplotlib — 資料視覺化。Data visualization.
- Jupyter Notebook — 互動式分析。Interactive analysis.

---

## 輸出與展示 | Outputs and Demos

### 問卷測試值分布 | Questionnaire Testing Value Counts
顯示問卷回答的分布狀況。  
Shows the distribution of questionnaire responses.

![Questionnaire Testing Value Counts](assets/questionnaire_testing_value_counts.jpg)

### 因素負荷熱力圖 | Factor Loading Heat Map
顯示每個題目對各因素的貢獻程度。  
Displays each item's contribution to factors.

![Factor Loading Heat Map](assets/factor_loading_heat_map.jpg)

### 相關矩陣熱力圖 | Correlation Matrix Heat Map
顯示各變數間的相關強度。  
Shows the strength of correlations between variables.

![Correlation Matrix Heat Map](assets/correlation_matrix_heat_map.jpg)

---

## 注意事項 | Notes and Limitations

- 部分分析依賴敏感資料（如原始問卷檔案），基於隱私保護原則，敏感檔案不公開於本 repository。Some analyses rely on sensitive data; for privacy and data protection reasons, sensitive files are not publicly available.
- 支援 Google Colab 進行雲端執行。Supports Google Colab for cloud-based execution.

---

## 研究方法與特色 | Research Methods & Features

- **資料前處理 | Data Preprocessing**：使用 pandas 與 pyreadstat 處理 .sav 問卷檔案。Handles .sav survey files using pandas and pyreadstat.
- **因素分析 | Factor Analysis**：使用 factor_analyzer 與 sklearn 進行因素分析。Conducts factor analysis using factor_analyzer and sklearn.
- **視覺化與洞察 | Visualization & Insights**：探索個人化、互動性與線上整合等學習因素間的關聯。Explores relationships between learning factors such as personalization, interaction, and online integration.
- **Colab 相容 | Colab Compatibility**：支援透過 Google Colab 進行雲端執行。Designed for cloud-based execution via Google Colab.

---

## 相關連結 | Related Links

- [專案 Catalog | Project Catalog](../../catalog/index.md)
- [Repository 根目錄 | Repository Root](../../README.md)
