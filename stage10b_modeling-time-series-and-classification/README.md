# Stage 10b — Modeling: Time Series & Classification

This folder contains a complete, runnable baseline that **creates lag/rolling features** and **trains a classifier to predict next-step direction** on a synthetic time series.  
It follows the assignment structure (Data → Features → Target → Split → Pipeline → Metrics → Interpretation) and is ready to drop into your repo.

## Contents
- `notebooks/stage10b_modeling_time_series_and_classification.ipynb` — fully worked notebook (classification baseline).
- `notebooks/stage10b_modeling-time-series-and-classification_homework-starter.ipynb` — provided starter (kept for reference).
- `docs/stage10b_modeling-time-series-and-classification_homework-sheet.pdf` — assignment sheet (copied here).
- `src/utils.py` — tiny helpers (paths, plotting, evaluation).
- `data/processed/` — output predictions and plots will be saved here.

## How to run (conda or venv)
```bash
# Optional: create env
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
# Open notebooks/stage10b_modeling_time_series_and_classification.ipynb and Run All
```

## What this notebook does
1. Generates a synthetic daily return series with mild autocorrelation (AR(1)+noise).
2. Engineers **leakage-safe** features: `lag_1`, `lag_5`, `roll_mean_5`, `roll_std_5`, `momentum_5`, `zscore_5`.
3. Sets `y_up = (ret.shift(-1) > 0).astype(int)` as the next-step direction target.
4. Uses **time-aware split** (TimeSeriesSplit) and also reports a **holdout** performance.
5. Builds an `sklearn` **Pipeline**: `StandardScaler` → `LogisticRegression`.
6. Evaluates with **accuracy, precision, recall, F1**, **confusion matrix**, and **prediction-over-time** plots.
7. Saves metrics and figures to `data/processed/`.

> Swap in your own time series by replacing the synthetic generator with your dataset load—keep the split and pipeline patterns the same.

## Requirements covered
- Feature engineering (multiple lag/rolling/momentum/zscore features).
- Time-aware split (no leakage).
- Pipeline (preprocessing → model).
- Metrics & plots for classification.
- Short interpretation at the end.
