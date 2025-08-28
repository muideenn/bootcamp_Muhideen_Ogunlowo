
"""
Train a simple Linear Regression model on synthetic data and save to model/model.pkl
"""
from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

from src.utils import save_df, save_model, project_path

RNG = np.random.default_rng(42)

# Synthetic regression: y = 3*x1 - 2*x2 + noise
n = 400
x1 = RNG.normal(0, 1, n)
x2 = RNG.normal(0, 1, n)
X = np.column_stack([x1, x2])
y = 3.0 * x1 - 2.0 * x2 + RNG.normal(0, 0.5, n)

df = pd.DataFrame({"x1": x1, "x2": x2, "y": y})
save_df(df, "data/processed/synth_train.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)
model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

save_model(model, "model/model.pkl")

metrics = {"r2": float(r2), "mae": float(mae)}
Path(project_path("reports/train_metrics.json")).write_text(__import__("json").dumps(metrics, indent=2))
print("Saved model to model/model.pkl")
print("Metrics:", metrics)
