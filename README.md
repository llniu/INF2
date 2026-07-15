# INF-2: Symbolic Regression for Non-invasive Detection of Hepatic Inflammation in Steatotic Liver Disease

This repository contains the analysis code used for the development and evaluation of **INF-2**, a symbolic regression-based blood biomarker for detecting hepatic inflammation and steatohepatitis at risk of progression in patients with steatotic liver disease (SLD).

The repository reproduces the complete analysis workflow described in the accompanying manuscript, including data preprocessing, exploratory analyses, feature selection, symbolic regression model development, model validation, sensitivity analyses, and ROC comparisons.

---

## Manuscript

**Title**

*Development and validation of a novel non-invasive INF-2 biomarker for inflammation in steatotic liver disease*

**Abstract**

Current interventions for steatotic liver disease (SLD) aim to attenuate hepatic inflammation, reducing liver-related morbidity and mortality. Yet, accurate circulating biomarkers of hepatic inflammation and at-risk steatohepatitis are lacking. We developed and validated symbolic regression models using targeted plasma proteomics to identify simple blood-based diagnostic signatures.

The final model (INF-2), consisting of ** two proteins **, accurately identified:

- Mild hepatic inflammation
- Steatohepatitis at risk of progression

across multiple SLD etiologies with performance comparable to elastography-based scores.

---

# Repository structure

```
.
├── src/                                # Shared utility functions
├── symbolic_regression/                # Symbolic regression implementation
├── roc_comparison/                     # ROC comparison utilities
│
├── 01_Olink_data_processing.ipynb
├── 02_Olink_baseline_characteristics.ipynb
├── 03_Olink_exploratory.ipynb
├── 04_Olink_mrmr.ipynb
├── 05_Olink_symbolic_regression_models.ipynb
├── 06_Olink_symbolic_regression_model_performance.ipynb
├── 07_Olink_sensitivity_analyses.ipynb
├── 08_Olink_sh_at_risk_progression.ipynb
├── 09_assignment_of_inflammation_score.txt
│
└── README.md
```

---

# Analysis workflow

The notebooks are intended to be run sequentially.

## 1. Data processing

`01_Olink_data_processing.ipynb`

- Import raw Olink proteomics data
- Quality control
- Missing value handling
- Data cleaning
- Creation of analysis datasets

---

## 2. Baseline characteristics

`02_Olink_baseline_characteristics.ipynb`

- Cohort demographics
- Clinical characteristics
- Summary statistics
- Tables for the manuscript

---

## 3. Exploratory analyses

`03_Olink_exploratory.ipynb`

- Protein distributions
- Correlation analyses
- Initial biomarker exploration
- Visualization

---

## 4. Feature selection

`04_Olink_mrmr.ipynb`

Minimum Redundancy Maximum Relevance (mRMR) feature selection was used to identify informative candidate proteins prior to symbolic regression.

---

## 5. Symbolic regression

`05_Olink_symbolic_regression_models.ipynb`

Development of symbolic regression classification models combining plasma proteins with routine liver enzymes (AST/ALT).

This notebook generates candidate equations and ranks models based on predictive performance.

---

## 6. Model evaluation

`06_Olink_symbolic_regression_model_performance.ipynb`

Evaluation of candidate models on:

- Derivation cohort
- Independent validation cohort

Metrics include:

- AUROC
- Sensitivity
- Specificity
- PPV
- NPV
- ROC curves
- F1 score
- MCC

---

## 7. Sensitivity analyses

`07_Olink_sensitivity_analyses.ipynb`

Assessment of model robustness across:

- Disease etiologies
- Fibrosis stages
- Clinical subgroups

---

## 8. Steatohepatitis at-risk analyses

`08_Olink_sh_at_risk_progression.ipynb`

Evaluation of symbolic regression models for identifying patients with steatohepatitis at risk of progression (NAS ≥4 with fibrosis ≥F2).

Includes comparison with established clinical scores like FAST.

---

## 9. Inflammation score assignment

`09_assignment_of_inflammation_score.txt`

Description of the final inflammation score assignment used in downstream analyses.

---

# Data availability

The patient-level datasets used in this study cannot be publicly released due to institutional ethics approvals and participant privacy restrictions.

Example notebooks and code are provided to enable full methodological transparency and reproducibility.

---

# Requirements

Main Python packages include:

- Python ≥3.10
- pandas
- numpy
- scipy
- pingouin
- scikit-learn
- matplotlib
- seaborn
- statsmodels
- feyn

A reproducible environment can be created using:

```bash
conda env create -f environment.yml
```
---

# Outputs

The notebooks generate:

- Publication figures
- ROC curves
- Feature rankings
- Symbolic regression equations
- Model performance metrics
- Supplementary tables

---

# Citation

If you use this repository, please cite:

> *Niu et al., Development and validation of a novel non-invasive INF-2 biomarker for inflammation in steatotic liver disease (Unpublished)*

---

# License

This repository is distributed under the terms of the LICENSE included in this repository.

---


