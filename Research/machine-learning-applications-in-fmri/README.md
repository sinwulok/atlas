# machine-learning-applications-in-fmri

Machine learning applications for functional MRI analysis and research.

---

## Overview

This repository showcases practical applications of machine learning techniques on functional MRI (fMRI) data using the Nilearn library. It includes hands-on exercises and example workflows such as CanICA, dictionary learning, and functional connectivity analysis, adapted from the official Nilearn documentation.

**Note**: This project is intended solely for educational and personal study purposes.

---

## Category / Lifecycle / Tags

- **Category**: Research
- **Type**: Machine Learning | fMRI
- **Lifecycle**: stable
- **Tags**: machine-learning, fmri, research

---

## Structure

```
Research/machine-learning-applications-in-fmri/
├── assets/                 # Diagrams and result images
├── notebooks/              # Jupyter notebooks
└── README.md               # This file
```

---

## How to Run

1. Install dependencies:
   ```bash
   pip install nilearn scikit-learn numpy matplotlib
   ```

2. Run the Jupyter notebooks for fMRI analysis

3. View results in the `assets/` directory

---

## Dependencies

- Nilearn
- Scikit-learn
- NumPy
- Matplotlib

---

## Outputs / Demos

### Research Workflow Diagram
![Research Workflow Diagram](assets/machine-learning-on-fmri-research-workflow-diagram-v4.drawio.svg)

### Research Result of ROI
![result_1](assets/images/group-icawithdictlearn-01.png)
![result_2](assets/images/group-icawithdictlearn-02.png)
![result_3](assets/images/group-icawithdictlearn-03.png)

### Research Result of Comparison
![result_comparison_1](assets/images/compair_extrac.PNG)

### Research Result of Region
![result_region_1](assets/images/corr_regions_of_DtL.JPG)

### Research Result of Visualization
![result_visualization_1](assets/images/connectome_2d.PNG)
![result_visualization_2](assets/images/connectome_3d.PNG)

---

## Notes / Limitations

- For educational and personal study purposes only
- Not for commercial use or distribution
- Adapted from Nilearn documentation examples

---

## Related Links

- [Nilearn Official Documentation](https://nilearn.github.io/)
- [Nilearn GitHub Repository](https://github.com/nilearn/nilearn/)
- [Project Catalog](../../catalog/index.md)
- [Repository Root](../../README.md)

---

## Acknowledgments

Nilearn enables approachable and versatile analyses of brain volumes. It provides statistical and machine-learning tools, with instructive documentation & friendly community.

### Reference

Abraham Alexandre, Pedregosa Fabian, Eickenberg Michael, Gervais Philippe, Mueller Andreas, Kossaifi Jean, Gramfort Alexandre, Thirion Bertrand, Varoquaux Gael (2014). "Machine Learning for Neuroimaging with scikit-learn". *Frontiers in Neuroinformatics*, Volume 8, Pages 14. DOI: [10.3389/fninf.2014.00014](https://doi.org/10.3389/fninf.2014.00014)
