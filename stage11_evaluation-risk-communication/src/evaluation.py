from __future__ import annotations
import numpy as np
import pandas as pd
from typing import Callable, Tuple
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.impute import SimpleImputer

def generate_synthetic_data(n: int = 800, missing_rate: float = 0.08, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = rng.choice(list("ABCD"), size=n, p=[0.35, 0.35, 0.2, 0.1])
    x1 = rng.normal(0, 1, n)
    x2 = rng.normal(0, 1.2, n) + 0.6*(seg=='C') - 0.4*(seg=='D')
    x3 = rng.uniform(-1, 1, n)
    noise = rng.normal(0, 0.7, n) + 0.3*(seg=='D')
    y = 2.0 + 1.2*x1 - 0.8*x2 + 0.5*x3 + noise

    df = pd.DataFrame({"y": y, "x1": x1, "x2": x2, "x3": x3, "segment": seg})
    mask = rng.random(df.shape) < missing_rate
    for c in ["x1","x2","x3"]:
        df.loc[mask[:, list(df.columns).index(c)], c] = np.nan
    return df

def simple_model_fit_predict(X: pd.DataFrame, y: pd.Series):
    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict(X)
    return model, pred

def rmse(y_true, y_pred) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))

def mae(y_true, y_pred) -> float:
    return float(mean_absolute_error(y_true, y_pred))

def bootstrap_metric_ci(X, y, metric_fn: Callable, B: int = 1000, seed: int = 123, return_dist=False):
    rng = np.random.default_rng(seed)
    n = len(y)
    stats = np.empty(B)
    for b in range(B):
        idx = rng.integers(0, n, n)
        Xb = X.iloc[idx]
        yb = y.iloc[idx]
        _, pred_b = simple_model_fit_predict(Xb, yb)
        stats[b] = metric_fn(yb, pred_b)
    ci_lo, ci_hi = np.percentile(stats, [2.5, 97.5])
    point_est = float(np.mean(stats))
    return (float(ci_lo), float(ci_hi)), point_est, (stats if return_dist else np.array([]))

def scenario_impute(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    out = df.copy()
    feat = ["x1","x2","x3"]
    imputer = SimpleImputer(strategy=strategy)
    out[feat] = imputer.fit_transform(out[feat])
    return out

def scenario_drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=["x1","x2","x3","y"]).reset_index(drop=True)

def subgroup_metric_by(df: pd.DataFrame, metric_fn: Callable, subgroup_col: str = "segment") -> pd.DataFrame:
    rows = []
    for g, gdf in df.groupby(subgroup_col, dropna=False):
        Xg = gdf[["x1","x2","x3"]]
        yg = gdf["y"]
        _, pg = simple_model_fit_predict(Xg, yg)
        rows.append({"segment": g, "n": len(gdf), "rmse": rmse(yg, pg), "mae": mae(yg, pg)})
    return pd.DataFrame(rows).sort_values("segment").reset_index(drop=True)