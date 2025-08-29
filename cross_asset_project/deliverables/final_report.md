
# Cross-Asset Correlation Analysis — Stakeholder Summary

## Executive Summary
- The equity–bond relationship is **time‑varying**. Using rolling correlation as a feature improves signal on equity next‑day direction.
- Our best baseline (RandomForest) achieves **F1 ≈ 0.532** on out‑of‑sample data, with **bootstrap 95% CI** indicating stability within a narrow range.
- Performance **degrades in high‑volatility regimes**; decisions should be more conservative when 20‑day equity volatility is in the top quartile.

## Key Visuals
1. `rolling_corr_20.png`: Rolling equity–bond correlation (signal driver).
2. `confusion_matrix_rf.png`: Out‑of‑sample classification results.
3. `f1_ci_scenarios.png`: Bootstrap confidence intervals across modeling/scenario assumptions.
4. `subgroup_correctness.png`: Accuracy contrast in low vs high volatility regimes.

## Assumptions & Risks
- Features use **only past information** (no leakage). Synthetic data proxies real‑world stylized facts.
- The **correlation window** (20–60 days) is a design choice; longer windows smooth noise but react slower to regime shifts.
- Model performance is **sensitive to volatility regime**; when volatility is high (≥ Q3), accuracy drops — treat predictions as lower confidence.
- Results assume **stable data schema** and similar missingness; major data quality issues would require re‑tuning.

## Sensitivity Summary
- Switching from 20‑day to 60‑day correlation slightly changes F1 (see CI bars); **RandomForest (20d)** remains best on our test period.
- A simpler **Logistic Regression** trails the RandomForest in F1, suggesting **nonlinearities** in the signal are important.

## Decision Implications
- Use the RF model for directional bias **only when volatility is below the upper‑quartile threshold**.
- When high volatility is detected, **tighten risk limits** (smaller position size or require stronger ensemble confirmation).
