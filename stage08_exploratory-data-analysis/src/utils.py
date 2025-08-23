from __future__ import annotations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

RAW_FILE = Path(__file__).resolve().parents[1] / "data" / "raw" / "outliers_homework.csv"
PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

def load_or_generate(seed: int = 42) -> pd.DataFrame:
    """Load the project CSV if present; otherwise generate a synthetic dataset."""
    if RAW_FILE.exists():
        df = pd.read_csv(RAW_FILE)
        return df
    rng = np.random.default_rng(seed)
    n = 1500
    df = pd.DataFrame({
        "customer_id": np.arange(1, n+1),
        "income": rng.normal(60000, 15000, n).round(2),
        "credit_score": np.clip(rng.normal(680, 50, n).round(), 300, 850).astype(int),
        "monthly_spend": np.abs(rng.normal(2000, 600, n)).round(2),
        "region": rng.choice(["North","South","East","West"], n),
        "default_flag": rng.choice([0,1], n, p=[0.82,0.18]).astype(int),
        "signup_date": pd.to_datetime("2022-01-01") + pd.to_timedelta(rng.integers(0, 900, n), unit="D")
    })
    # add some missingness and a few outliers
    miss_idx = rng.choice(n, size=60, replace=False)
    df.loc[miss_idx, "income"] = np.nan
    out_idx = rng.choice(n, size=8, replace=False)
    df.loc[out_idx, "monthly_spend"] *= 6
    return df

def missing_report(df: pd.DataFrame) -> pd.DataFrame:
    miss = df.isna().sum().to_frame("missing_count")
    miss["missing_pct"] = (miss["missing_count"] / len(df) * 100).round(2)
    return miss

def save_processed(df: pd.DataFrame, name: str = "eda_processed.csv") -> Path:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    path = PROCESSED_DIR / name
    df.to_csv(path, index=False)
    return path

def quick_hist(df: pd.DataFrame, col: str, bins: int = 30):
    plt.figure(figsize=(7,4))
    df[col].plot.hist(bins=bins)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def quick_box(df: pd.DataFrame, col: str):
    plt.figure(figsize=(5,4))
    df[[col]].plot.box()
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.show()

def quick_scatter(df: pd.DataFrame, x: str, y: str):
    plt.figure(figsize=(6,5))
    plt.scatter(df[x], df[y], alpha=0.5)
    plt.title(f"Scatter: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()
