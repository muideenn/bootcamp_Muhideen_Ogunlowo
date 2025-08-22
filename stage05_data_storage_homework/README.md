# Stage 05 — Data Storage

This repository implements a small, reproducible storage layer for a pandas DataFrame with utilities to read and write CSV/Parquet and to validate reloads.

## Data Storage

**Folder structure**
```
data/
  raw/         # source snapshots (CSV)
  processed/   # cleaned/curated artifacts (Parquet)
notebooks/
src/
```

**Formats**
- **CSV** in `data/raw/` for human-readable snapshots and portability.
- **Parquet** in `data/processed/` for efficient analytics (columnar, compressed).

**Environment-driven paths**
Paths are read from environment variables (configure via `.env`):
```
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```
The notebook and utilities resolve output/input locations using these values, so you can move the repo anywhere without changing code.

**Utilities**
`src/utils.py` exposes:
- `write_df(df, path)` → writes CSV/Parquet by suffix, creates parent dirs, and fails clearly if Parquet engine is missing.
- `read_df(path, dtype_map=None)` → reads by suffix and optionally enforces dtypes.
- `validate_df(original, reloaded, critical_dtypes)` → checks shape and dtypes of critical columns for reproducible reloads.

**Example outputs (created by running the notebook)**
- `data/raw/sample_YYYYMMDD-HHMM.csv`
- `data/processed/sample_YYYYMMDD-HHMM.parquet`

## How to run

Install requirements, set environment variables via `.env`, then open the notebook in `notebooks/` and execute cells.
