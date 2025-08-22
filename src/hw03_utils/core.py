from __future__ import annotations
import time
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def time_loop_vs_vectorized(n: int = 1_000_000) -> dict:
    """Compare Python loop vs NumPy vectorized operation on squaring numbers."""
    arr = np.arange(n, dtype=np.float64)

    t0 = time.perf_counter()
    out_loop = np.empty_like(arr)
    for i in range(n):
        out_loop[i] = arr[i] * arr[i]
    loop_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    out_vec = arr * arr
    vec_time = time.perf_counter() - t0

    assert np.allclose(out_loop, out_vec)
    return {
        "n": n,
        "loop_seconds": loop_time,
        "vectorized_seconds": vec_time,
        "speedup": loop_time / vec_time if vec_time > 0 else float("inf"),
    }


def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return numeric summary stats similar to DataFrame.describe()."""
    return (
        df.select_dtypes(include="number")
        .describe()
        .T.reset_index()
        .rename(columns={"index": "column"})
    )


def _pick_category_column(df: pd.DataFrame) -> Optional[str]:
    for col in df.columns:
        if df[col].dtype == "object" or str(df[col].dtype).startswith("category") or df[col].nunique() <= 20:
            return col
    # If none, try creating one from first numeric column via bins
    num_cols = df.select_dtypes(include="number").columns.tolist()
    if not num_cols:
        return None
    col = num_cols[0]
    bins = pd.qcut(df[col], q=min(4, max(2, df[col].nunique())), duplicates="drop")
    df["auto_category"] = bins.astype(str)
    return "auto_category"


def groupby_aggregate(df: pd.DataFrame, agg_map: Optional[dict] = None) -> pd.DataFrame:
    """Perform a simple groupby aggregation on an inferred category column."""
    if df.empty:
        return df
    cat_col = _pick_category_column(df)
    if cat_col is None:
        return pd.DataFrame()
    if agg_map is None:
        # default: mean for numeric columns
        agg_map = {c: "mean" for c in df.select_dtypes(include="number").columns}
    out = df.groupby(cat_col).agg(agg_map)
    out.index.name = cat_col
    return out.reset_index()


def basic_histogram(series: pd.Series, title: str = "Basic Histogram", save_path: Optional[Path] = None) -> Optional[Path]:
    """Create a basic histogram for a numeric series and optionally save it."""
    plt.figure()
    series = pd.to_numeric(series, errors="coerce").dropna()
    if series.empty:
        return None
    plt.hist(series, bins=30)
    plt.title(title)
    plt.xlabel(series.name or "value")
    plt.ylabel("count")
    out_path = None
    if save_path is not None:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")
        out_path = save_path
    plt.close()
    return out_path


def save_plot(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path, bbox_inches="tight")