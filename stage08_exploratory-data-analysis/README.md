# Stage 08 — Exploratory Data Analysis (EDA)

This folder contains a complete, runnable EDA workflow that meets the homework requirements.

## Quick Start

1. (Optional) Put your dataset at `data/raw/outliers_homework.csv`.  
   If the file is missing, the notebook will generate a synthetic dataset with a similar schema.
2. Launch JupyterLab and open the notebook:
   ```bash
   jupyter lab notebooks/eda_muideenn.ipynb
   ```
3. Run all cells. Outputs (figures, profiles) will be created in-line. A processed CSV will be saved to `data/processed/`.

## Contents
- `notebooks/eda_muideenn.ipynb` — main notebook with:
  - `.info()`, `.describe()`, missing values profile
  - Histograms/boxplots for multiple variables
  - Bivariate relationships (scatter/line)
  - Optional correlation heatmap
  - Clear markdown for findings, assumptions, risks, and next steps
- `src/utils.py` — helper functions (safe loading, quick plots, missing report, and save utilities)
- `data/raw/` — drop raw CSVs here (kept empty by default)
- `data/processed/` — where cleaned or exported files will be written
- `docs/` — add your assignment PDF here if needed

## Requirements
- Python 3.11+
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

Install (conda example):
```bash
conda install -c conda-forge pandas numpy matplotlib seaborn scikit-learn
```

## Notes
- The notebook is defensive: it will create synthetic data if your raw file is missing.
- Plots have clear titles/labels and short commentary per plot.
- The last section summarizes Top 3 insights and Assumptions & Risks, plus next steps.
