# Refactor Demo — Rolling Correlation

This demo exposes a reusable function + CLI to compute rolling correlations between an equity and a bond series.

## Usage
```bash
python refactor_demo/compute_rolling_corr.py   --prices data/processed/clean.parquet   --eq-col SPY --bond-col TLT   --window 60   --out data/processed/rolling_corr.csv
```

- Logs: `logs/rolling_corr.log`
- Checkpoint: `data/processed/rolling_corr.ok`
