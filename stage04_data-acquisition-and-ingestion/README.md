
# Stage 04 — Data Acquisition & Ingestion

This repo pulls one market-related dataset via API (FRED) and scrapes a simple public table (Wikipedia), validates, and writes timestamped CSVs to `data/raw/`.

## Quickstart
```bash
# from repo root
pip install -r requirements.txt   # or: conda activate fe-course && pip install -r requirements.txt
python -c "import pandas, requests; print('OK')"
```

Open the notebook at `notebooks/stage04_data-acquisition-and-ingestion.ipynb` and run all cells.

## Secrets
- Put your FRED key in `.env` as `FRED_API_KEY=...`
- Do **not** commit `.env`. A safe `.env.example` is provided.

## Outputs
- `data/raw/api_FRED_DGS10_<UTC-TIMESTAMP>.csv`
- `data/raw/scrape_wikipedia_sp500_table_<UTC-TIMESTAMP>.csv`
