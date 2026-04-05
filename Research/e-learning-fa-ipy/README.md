# e-learning-fa-ipy

E-learning data analysis using Jupyter notebooks with preprocessing, modeling, and visualization.

---

## Overview

This project focuses on analyzing and exploring E-learning data, including preprocessing, statistical analysis, modeling, and visualization, primarily using Jupyter Notebook for interactive analysis.

---

## Category / Lifecycle / Tags

- **Category**: Research
- **Type**: Machine Learning | Functional Component Analysis
- **Lifecycle**: stable
- **Tags**: machine-learning, jupyter, education

---

## Structure

```
Research/e-learning-fa-ipy/
├── data/                   # Datasets (.sav files)
├── notebooks/              # Jupyter Notebook files
├── scripts/                # Reusable Python scripts
├── results/                # Analysis results and visualizations
├── assets/                 # Result images
└── README.md               # This file
```

---

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas pyreadstat factor-analyzer scikit-learn matplotlib jupyter
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open and run the analysis notebooks

4. View results in the `results/` and `assets/` directories

---

## Dependencies

- pandas - Data manipulation
- pyreadstat - Handling .sav files
- factor_analyzer - Factor analysis
- scikit-learn - Decomposition & modeling
- matplotlib - Data visualization
- Jupyter Notebook - Interactive analysis

---

## Outputs / Demos

### Questionnaire Testing Value Counts
Shows the distribution of questionnaire responses.

![Questionnaire Testing Value Counts](assets/questionnaire_testing_value_counts.jpg)

### Factor Loading Heat Map
Displays each item's contribution to factors.

![Factor Loading Heat Map](assets/factor_loading_heat_map.jpg)

### Correlation Matrix Heat Map
Shows the strength of correlations between variables.

![Correlation Matrix Heat Map](assets/correlation_matrix_heat_map.jpg)

---

## Notes / Limitations

- Some analyses rely on sensitive data (e.g., original questionnaire files)
- For privacy and data protection reasons, sensitive files are not publicly available in this repository
- Supports Google Colab for cloud-based execution

---

## Research Methods & Features

- **Data Preprocessing**: Handles .sav survey files using pandas and pyreadstat
- **Factor Analysis**: Conducts factor analysis using factor_analyzer and sklearn
- **Visualization & Insights**: Explores relationships between learning factors such as personalization, interaction, and online integration
- **Colab Compatibility**: Designed for cloud-based execution via Google Colab

---

## Related Links

- [Project Catalog](../../catalog/index.md)
- [Repository Root](../../README.md)
