# Applied Financial Engineering — Framework Guide (Completed)

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|---|---|---|---|---|
| **1. Problem Framing & Scoping** | Framed *Cross‑Asset Correlation Analysis* to study equity–bond correlation dynamics for portfolio diversification. Defined success as clear regime‑level insights and reproducible code. | Ambiguity about regime definitions and sample windows. | Scoped to major benchmarks and rolling windows (e.g., 60–252 days). Set measurable outcomes (plots + summary tables). | Formal regime definitions using macro indicators or HMMs. |
| **2. Tooling Setup** | Conda env, Python 3.11, pinned `requirements.txt`, `make` targets for lint/test/run. | Version drift and OS differences. | Locked versions; added quickstart in README. | Add dev containers and CI cache. |
| **3. Python Fundamentals** | Vectorized pandas ops, pathlib I/O, modular utils. | Occasional chained assignment and dtype warnings. | Strict data types; helper funcs for safe I/O. | More unit tests for utils. |
| **4. Data Acquisition / Ingestion** | Pulled benchmark prices (CSV/APIs), aligned trading days. | Missing days / market holidays. | Left‑join on a master calendar; forward‑filled only where appropriate. | Data contracts and schema validation. |
| **5. Data Storage** | Parquet for processed, CSV for raw; simple folder schema. | Mixed frequencies and symbols. | Normalized to tidy format with symbol/date keys. | Add metadata catalog (YAML). |
| **6. Data Preprocessing** | Log‑returns, outlier caps for clear errors, NaN handling. | Distinguishing bad ticks vs true shocks. | Rule‑based filters + audit trail of changes. | Robust filters (MAD, robust z‑scores). |
| **7. Outlier Analysis** | Detected extreme moves; compared caps vs keep. | Risk of removing informative stress events. | Kept true market shocks; capped obvious errors. | Model‑based anomaly detection. |
| **8. Exploratory Data Analysis (EDA)** | Rolling corr plots, KDEs, heatmaps; summary stats by regime. | Visual clutter and scale issues. | Standardized plotting utils; small multiples. | Add interactive dashboards. |
| **9. Feature Engineering** | Lags of returns, realized vol, drawdown flags, macro proxies. | Leakage risk and sparse features. | Strict train/test splits and lagged features only. | Macro‑aware state features. |
| **10. Modeling** | Baseline: rolling OLS of corr drivers; optional regime classifier. | Instability & overfitting. | Penalization, cross‑validation, and holdout periods. | Markov‑switching or TVP models. |
| **11. Evaluation & Risk Communication** | Evaluated regime identification accuracy and allocation outcomes. | Non‑stationarity and uncertainty communication. | Reported confidence bands and sensitivity tests. | Broader scenarios, bootstrap CIs. |
| **12. Reporting & Stakeholder Communication** | README, plots, and stakeholder summary document. | Translating stats to portfolio impact. | Focused on risk narratives and simple allocations. | Add “what‑if” dashboard. |
| **13. Productization** | Modular `src/` with clear interfaces; CLI entry points. | Reproducibility and drift. | Frozen seeds, deterministic pipelines. | Data versioning (DVC) and artifacts. |
| **14. Deployment & Monitoring** | Local batch runs; checks for data staleness. | Detecting silent data failures. | Lightweight validation before compute. | Add alerts and logging to remote store. |
| **15. Orchestration & System Design** | DAG of tasks: ingest→clean→corr→report; idempotent file targets. | Dependency order and retries. | Declarative task graph and atomic writes. | Move to Airflow/Prefect for scheduling. |
| **16. Lifecycle Review & Reflection** | Consolidated lessons and tightened repo polish. | Balancing completeness vs simplicity. | Prioritized clarity, documented tradeoffs. | Expand assets, automate checks. |
