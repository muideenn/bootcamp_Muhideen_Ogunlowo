# Reflection — Deployment & Monitoring (Stage 14)

**Context.** The project analyzes **cross‑asset correlations** (equities ↔ bonds) to inform hedge ratios and diversification decisions. If deployed, the main risks are: (1) **schema/data drift** (vendor adds/removes fields or units change), (2) **distribution shift** during macro regime changes (e.g., policy shocks that flip sign of correlations), (3) **label/ground‑truth delay** for realized returns, (4) **pipeline fragility** (late batches, partial loads), and (5) **model staleness** as relationships decay.

**What we monitor.**
- **Data layer:** ingest freshness (max minutes since last successful batch), null rate per key field, schema hash, and **PSI** on top features (target: PSI < 0.1; warn at 0.2). Thresholds: nulls < 1%, freshness < 30 min for intraday; < 6 hrs for EOD.
- **Model layer:** rolling 20‑day error for correlation forecasts (MAE target < 0.10), calibration of hedge ratio effectiveness (tracking error vs. benchmark), and drift in feature importances. Retrain when 2‑week MAE ≥ 0.15 or PSI ≥ 0.2 on ≥ 2 features.
- **System layer:** ETL/job success rate (≥ 99%), p95 API latency (< 300 ms), and uptime (≥ 99.5%). Alerts page on on‑call if two consecutive failures occur.
- **Business layer:** realized diversification benefit (portfolio variance reduction vs. baseline), VaR breach count attributable to correlation error, and **decision KPI** (e.g., hedge P&L hit rate ≥ 55%).

**Ownership & handoffs.** Data Engineering owns ingestion freshness/schema validation; Quant Research owns model metrics and retraining; Platform SRE owns runtime, alerting, and rollbacks. First‑responder: Platform on‑call (triage), then route by label (data/model/system). Issues logged in the tracker with runbook links; rollbacks require Quant + Platform approval. Weekly analytics review confirms KPI alignment; quarterly review revisits thresholds and retraining cadence.
