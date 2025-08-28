# Orchestration Plan — Cross‑Asset Correlation Analysis (Stage 15)

## 1) Pipeline DAG (high level)
```mermaid
flowchart TD
    A[Ingest market data] --> B[Clean & align]
    B --> C[Feature engineering]
    C --> D[Rolling correlations]
    D --> E[Regime detection / stress tagging]
    E --> F[Reports & charts]
    C --> G[Modeling (optional)]
    B --> H[Data quality checks]
```
Parallelizable: `H` can run in parallel with `C` once `B` completes.

## 2) Tasks with I/O, Idempotency, Logging, Checkpoints
| ID | Task | Inputs | Outputs | Idempotent? | Logging | Checkpoint |
|---|---|---|---|:--:|---|---|
| A | Ingest market data (FRED, Yahoo/CSV) | API keys, tickers list | `data/raw/*.csv` | Yes (same date range → same files) | `logs/ingest.log` | `.ok` files per source |
| B | Clean & align (time index, fill, FX) | `data/raw/*.csv` | `data/processed/clean.parquet` | Yes | `logs/clean.log` | `data/processed/clean.ok` |
| C | Feature engineering (returns, lags) | `clean.parquet` | `data/processed/features.parquet` | Yes | `logs/features.log` | `features.ok` |
| D | Rolling correlations (eq–bond) | `features.parquet` | `data/processed/rolling_corr.csv` | Yes | `logs/rolling_corr.log` | `rolling_corr.ok` |
| E | Regime detection (e.g., z-score/Markov) | `rolling_corr.csv` | `data/processed/regimes.parquet` | Yes | `logs/regimes.log` | `regimes.ok` |
| F | Reports & charts | previous outputs | `docs/report.md`, `docs/fig_*` | Yes | `logs/report.log` | `report.ok` |
| G | Modeling (optional) | `features.parquet` | `models/*.pkl`, metrics | Yes | `logs/model.log` | `model.ok` |
| H | Data quality checks | `raw/*.csv` | `docs/dq_report.md` | Yes | `logs/dq.log` | `dq.ok` |

- **Idempotency**: All tasks overwrite or version their outputs; safe to re-run.
- **Interfaces**: File I/O with explicit, stable paths; no hidden state.

## 3) Reliability: Logging, Checkpoints, Retries
- **Logging**: Python `logging` to `logs/<task>.log` with timestamps + INFO/ERROR levels.
- **Checkpoints**: zero-byte `.ok` files and/or the presence/mtime of expected outputs.
- **Retries**: For network-bound steps (A), retry 3× with exponential backoff; other steps fail-fast with clear messages.

## 4) Failure Points & Handling
- **API/network**: fall back to cached files; mark partial failure.
- **Schema drift**: validate columns before transform; abort with actionable error.
- **Time alignment**: enforce left-join on business days; assert no duplicate indices.

## 5) Right-sizing automation
Automate now: A–F (pure Python, deterministic file I/O).  
Keep manual (for now): credentials provisioning, chart curation for final report, and model hyperparameter exploration.  
Rationale: immediate payoff, minimal infra, aligns with the Stage 15 scope (functions + CLI + logging).

## 6) How to run (suggested order)
```bash
# From repository root, with this folder at ./stage15_orchestration-system-design
python refactor_demo/compute_rolling_corr.py --prices data/processed/clean.parquet \
    --eq-col SPY --bond-col TLT --window 60 --out data/processed/rolling_corr.csv
```
