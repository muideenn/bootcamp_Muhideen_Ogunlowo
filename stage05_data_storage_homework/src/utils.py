from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Dict
import pandas as pd

try:
    import pyarrow  # noqa: F401
    _HAS_PARQUET = True
except Exception:
    _HAS_PARQUET = False


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_df(df: pd.DataFrame, path: str | Path) -> Path:
    """
    Write a DataFrame to CSV or Parquet based on file suffix.
    Creates parent directories if they don't exist.
    Raises a clear error if parquet engine is missing.
    """
    p = Path(path)
    _ensure_dir(p.parent)
    suffix = p.suffix.lower()
    if suffix == ".csv":
        df.to_csv(p, index=False)
    elif suffix == ".parquet":
        if not _HAS_PARQUET:
            raise RuntimeError(
                "Parquet engine (pyarrow) not installed. "
                "Install pyarrow or choose a .csv path."
            )
        df.to_parquet(p, index=False)
    else:
        raise ValueError(f"Unsupported suffix '{suffix}'. Use .csv or .parquet.")
    return p


def read_df(path: str | Path, dtype_map: Optional[Dict[str, str]] = None) -> pd.DataFrame:
    """
    Read a DataFrame from CSV or Parquet based on file suffix.
    Optionally enforce dtypes for critical columns using dtype_map.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    suffix = p.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(p)
    elif suffix == ".parquet":
        if not _HAS_PARQUET:
            raise RuntimeError(
                "Parquet engine (pyarrow) not installed. "
                "Install pyarrow or read from a .csv instead."
            )
        df = pd.read_parquet(p)
    else:
        raise ValueError(f"Unsupported suffix '{suffix}'. Use .csv or .parquet.")
    if dtype_map:
        # Coerce columns that are present in df
        for col, dt in dtype_map.items():
            if col in df.columns:
                df[col] = df[col].astype(dt)
    return df


def validate_df(original: pd.DataFrame, reloaded: pd.DataFrame, critical_dtypes: Dict[str, str]) -> dict:
    """
    Compare shape and dtypes of critical columns.
    Returns a results dict with 'shape_match', 'dtype_issues', and 'passed'.
    """
    shape_match = original.shape == reloaded.shape
    dtype_issues = {}
    for col, expected in critical_dtypes.items():
        if col not in reloaded.columns:
            dtype_issues[col] = f"missing (expected {expected})"
        else:
            got = str(reloaded[col].dtype)
            if got != expected:
                dtype_issues[col] = f"{got} (expected {expected})"
    passed = shape_match and (len(dtype_issues) == 0)
    return {"shape_match": shape_match, "dtype_issues": dtype_issues, "passed": passed}
