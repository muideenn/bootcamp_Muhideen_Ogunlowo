# Stage 08 – Exploratory Data Analysis (EDA)

## Overview
This notebook (`stage08hw.ipynb`) performs a **comprehensive exploratory data analysis (EDA)** on a synthetic financial-behavior dataset.  
The goal is to simulate and analyze patterns in variables such as `income`, `spend`, `transactions`, `age`, and `credit_score`, while also exploring time-series trends.

Key analyses include:
- Data sanity checks (`.info()`, `.describe()`, missing values)  
- Univariate analysis (distributions, skewness, outliers)  
- Bivariate analysis (scatterplots, correlations, relationships)  
- Time-series decomposition (daily/weekly/monthly/yearly resampling, rolling averages)  
- Additive vs. multiplicative seasonal simulations  
- Correlation heatmaps and pairwise plots  
- A final **"So What?" Insights & Assumptions** section to prepare for Feature Engineering

---

## Notebook Structure
1. **Synthetic Data Generator** – Creates reproducible dataset with numeric & categorical variables.  
2. **Sanity Checks** – Inspect shape, missing values, data types.  
3. **Univariate Visuals** – Histograms, boxplots, outlier detection.  
4. **Bivariate Visuals** – Scatterplots of `age–income`, `income–transactions`, etc.  
5. **Time Series Glance** – Rolling means, cumulative sums, trend visualization.  
6. **Additive vs. Multiplicative Models** – Seasonal decomposition.  
7. **Correlation Matrix** – Heatmap to detect relationships and redundancy.  
8. **Helper Functions** – Reusable `eda_summary(df)` for quick stats.  
9. **Insights & Assumptions** – Key findings to guide feature engineering.  

---

## Requirements
The notebook uses standard Python data-science libraries:

```bash
conda install -c conda-forge \
    python=3.11 \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    jupyterlab
