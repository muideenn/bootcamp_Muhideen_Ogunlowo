# Stage 10a — Modeling: Linear Regression

**Folder:** `stage10a_modeling-linear-regression`

This stage fits a baseline Linear Regression model, evaluates assumptions with residual diagnostics, and reports **R²** and **RMSE**. The notebook is self‑contained and will use your cleaned dataset if available (e.g., `data/processed/clean.csv`). Otherwise, it generates synthetic data to prototype.

## Contents
- `notebooks/modeling_regression_muideenn.ipynb` — main notebook
- `src/utils.py` — small helper utilities
- `data/` — put your CSVs here (`data/processed/clean.csv` if you have one)
- `docs/stage10a_modeling-linear-regression_homework-sheet.pdf` — assignment sheet
- `requirements.txt` — minimal Python deps

## Quickstart
```bash
# (Optional) Create and activate a clean env
conda create -n fe-course python=3.11 -y
conda activate fe-course

# Install requirements
pip install -r requirements.txt

# Launch Jupyter
jupyter lab  # or: jupyter notebook
```

Open the notebook at `notebooks/modeling_regression_muideenn.ipynb` and **Run All**.

## Notes
- If `data/processed/clean.csv` exists with a numeric target column named `y` and numeric features in other columns, the notebook will auto‑use it.
- Otherwise, the notebook falls back to a reproducible synthetic dataset with known relationships.
- The notebook produces: Residuals vs Fitted, Residual Histogram, QQ plot, Residuals vs a key predictor, and Residual lag‑1 plot.
- An optional polynomial feature is included to demonstrate that adding a squared term can still be linear regression (linear in parameters).
