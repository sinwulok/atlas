# E-Learning-FA (2022-2023)

## 專案簡介 | Project Overview

本專案旨在分析與探討 E-Learning（線上學習）相關數據，內容涵蓋資料預處理、統計分析、模型建立及視覺化，並以 Jupyter Notebook 進行互動式分析。  
This project focuses on analyzing and exploring E-Learning data, including preprocessing, statistical analysis, modeling, and visualization, primarily using Jupyter Notebook.

## Features
- **Interactive Notebooks**: Use Jupyter Notebook for interactive data analysis and visualization.
- **Machine Learning**: Includes implementations and applications of various machine learning models.
- **Data Preprocessing**: Provides tools and methods for data cleaning, transformation, and processing.

## Directory Structure (ref.)
```plaintext
.
├── data/               # Datasets
├── notebooks/          # Jupyter Notebook files
├── scripts/            # Python scripts
├── results/            # Analysis results and model outputs
└── README.md           # Project description file
```
---

## 目錄結構 | Repository Structure

### 詳細說明 | Details:
- **`data/`**: 包含用於分析的資料集（含 `.sav` 等格式）。  
  Includes datasets like `.sav` used for analysis.
- **`notebooks/`**: 儲存互動式分析用的 Jupyter Notebook 檔案（如 `E-Learning-FA.ipynb`）。  
  Contains Jupyter Notebook files for interactive data exploration and analysis.
- **`scripts/`**: 放置可重複使用的 Python 腳本（如資料清理、轉換和視覺化）。  
  Holds reusable Python scripts for tasks such as data cleaning, transformation, or visualization.
- **`results/`**: 儲存分析結果、視覺化圖表及處理後的資料集。  
  Stores outputs such as visualizations, factor analysis results, or processed datasets.
- **`README.md`**: 提供專案總覽與使用說明。  
  Provides an overview of the project and instructions for usage.

---

## 實驗成果展示 | Experiment Results

### 問卷測試數值分布 | Questionnaire Testing Value Counts

Shows the distribution of questionnaire responses.

![問卷測試數值分布](assets/Questionnaire_Testing_Value_Counts.jpg)

### 因子負載量熱圖 | Factor Loading Heat Map

Displays each item's contribution to factors.

![因子負載量熱圖](assets/Factor_Loading_Heat_Map.jpg)

### 相關矩陣熱圖 | Correlation Matrix Heat Map

Shows the strength of correlations between variables.

![相關矩陣熱圖](assets/Correlation_Matrix_Heat_Map.jpg)

---

## 敏感資料說明 | Sensitive Data Notice

本專案部分分析需依賴敏感資料（如問卷原始檔案等），基於隱私與資料保護考量，這類檔案並未公開於本倉庫。  
Some analyses in this project rely on sensitive data. For privacy and data protection reasons, these files are not publicly available in this repository.

---

## 研究方法與功能 | Research Methods & Features

- **資料預處理 Data Preprocessing**：  
  使用 Python 套件（如 `pandas`, `pyreadstat`）處理 `.sav` 問卷資料。  
  Handles `.sav` survey files using Python libraries such as `pandas` and `pyreadstat`.
- **因子分析 Factor Analysis**：  
  利用 `factor_analyzer` 與 `sklearn` 進行問卷資料的因子分析。  
  Conducts factor analysis on the survey data using `factor_analyzer` and `sklearn`.
- **視覺化與洞察 Visualization & Insights**：  
  探討多種學習要素（如個人化、互動性、線上整合性）之間的關聯。  
  Explores relationships between multiple learning factors such as personalization, interaction, and online integration.
- **Colab 相容性 Colab Compatibility**：  
  支援 Google Colab 雲端執行與套件安裝。  
  Designed for cloud-based execution and easy library installation via Google Colab.

---

## 技術棧 | Technologies Used

- **Python Libraries**:
  - `pandas`：資料處理 Data manipulation
  - `pyreadstat`：處理 `.sav` 檔案 Handling `.sav` files
  - `factor_analyzer`：因子分析 Factor analysis
  - `sklearn`：降維與建模 Decomposition & modeling
  - `matplotlib`：資料視覺化 Data visualization
- **Jupyter Notebook**：互動式分析與視覺化 Interactive data analysis & visualization
- **Google Colab**：雲端協作與執行 Cloud-based execution & collaboration

---

## 聯絡方式 | Contact

如有任何問題或協作需求，歡迎於 Issue 區留言或聯絡專案維護者。  
For questions or collaboration, please open an issue or contact the project maintainer.

---

