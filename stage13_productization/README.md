
# Stage 13 — Productization (Demo Pack)

This folder is a self-contained demo of **productization** for a small regression model: clean repo structure, reusable code, model persistence, a Flask API, optional dashboard stub, and handoff-ready docs.

## Folder Structure

```
stage13_productization/
├── app.py
├── dashboard/
├── data/
│   ├── processed/
│   └── raw/
├── model/
│   └── model.pkl
├── notebooks/
│   ├── stage13_productization_homework-starter.ipynb
│   └── model_and_api_demo.ipynb  (optional placeholder)
├── reports/
│   ├── stakeholder_summary.pdf
│   └── train_metrics.json
├── src/
│   ├── train_model.py
│   └── utils.py
├── tests/
│   └── test_api_demo.py
├── requirements.txt
└── README.md
```

This layout matches the **homework sheet** guidance: organized repo, modularized code, model persistence, Flask endpoints, docs, and testing evidence. (See homework sheet.)

## Quickstart

```bash
# 1) Create venv / conda and install deps
python -m venv .venv && source .venv/bin/activate   # or use conda
pip install -r requirements.txt

# 2) Train the model (writes model/model.pkl and reports/train_metrics.json)
python -m src.train_model

# 3) Run the API
python app.py   # opens http://127.0.0.1:5000
```

### Example Requests

```bash
# POST with multiple rows
curl -X POST http://127.0.0.1:5000/predict   -H "Content-Type: application/json"   -d '{"features": [[1.0,2.0],[0.5,-1.2]]}'

# GET with one feature (x2 defaults to 0.0)
curl http://127.0.0.1:5000/predict/1.5

# GET with two features
curl http://127.0.0.1:5000/predict/1.5/-0.2

# Plot image
curl -o plot.png http://127.0.0.1:5000/plot
```

### Run Tests (optional)

```bash
pip install pytest
pytest -q
```

## Reproducibility

- Deterministic training seed is used for the synthetic dataset.
- `requirements.txt` pins core libraries needed to run the pipeline and API.
- A teammate can clone, install, train, and serve predictions end‑to‑end following the steps above.

## Dashboard (optional)

A `dashboard/` directory is provided as a stub in case you wish to add Streamlit later:

```bash
streamlit run dashboard/app.py  # after you create it
```

## Notes

- The small model here is intentionally simple and trained on synthetic data to demonstrate the productization workflow.
- For your actual project, replace `src/train_model.py` with your true training script/notebook, persist your real model into `model/model.pkl`, and update the API feature schema accordingly.
