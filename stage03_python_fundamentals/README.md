# Stage 03 — Python Fundamentals (Homework) — Fixed Utils

This version fixes the `utils` import problem by shipping a proper package (`hw03_utils`) and a `pyproject.toml` to be able to run `pip install -e .`.

## Quick start
```bash
conda create -n fe-course python=3.11 -y
conda activate fe-course
pip install -e .
jupyter notebook notebooks/hw03_python_fundamentals.ipynb
```
If you'd rather install, the notebook also appends `src` to `sys.path` as a fallback.

## Expected outputs
- `data/processed/summary.csv` and `summary.json`
- `figs/basic_hist.png`
