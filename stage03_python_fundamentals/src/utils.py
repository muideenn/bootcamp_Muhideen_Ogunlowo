
import time
from typing import Dict, Iterable, Optional, Tuple, Union

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Performance utility
# -----------------------------
def time_loop_vs_vectorized(n: int = 1_000_000) -> pd.DataFrame:
    """Compare a pure-Python loop vs a NumPy vectorized operation.

    Parameters
    ----------
    n : int, default=1_000_000
        Number of elements to process.

    Returns
    -------
    pd.DataFrame
        DataFrame with method names and elapsed seconds.
    """
    # Data
    x = np.random.rand(n)

    # Python loop
    t0 = time.perf_counter()
    s_loop = 0.0
    for val in x:
        s_loop += val * val
    t_loop = time.perf_counter() - t0

    # Vectorized (NumPy)
    t0 = time.perf_counter()
    s_vec = np.sum(x * x)
    t_vec = time.perf_counter() - t0

    return pd.DataFrame(
        {
            "method": ["python_loop", "numpy_vectorized"],
            "seconds": [t_loop, t_vec],
            "result_example": [s_loop, float(s_vec)],
        }
    )


# -----------------------------
# Summary statistics
# -----------------------------
def get_summary_stats(
    df: pd.DataFrame,
    groupby_col: Optional[str] = None,
    decimals: int = 2,
) -> pd.DataFrame:
    """Compute clean summary statistics for numeric columns, overall or by group.

    - Ignores NaNs by default (as pandas does)
    - Rounds to `decimals`
    - For grouped stats, applies count/mean/std/min/max to all numeric columns

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    groupby_col : str, optional
        Column to group by before aggregating. If None, compute overall stats.
    decimals : int, default=2
        Decimal places for rounding.

    Returns
    -------
    pd.DataFrame
        Summary table.
    """
    # Drop entirely empty columns
    df = df.dropna(axis=1, how="all")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        return pd.DataFrame()  # nothing numeric to summarize

    if groupby_col is None:
        stats = df[numeric_cols].describe().T  # index = column names
    else:
        if groupby_col not in df.columns:
            raise KeyError(f"groupby_col '{groupby_col}' not in DataFrame columns.")
        agg_spec = {col: ["count", "mean", "std", "min", "max"] for col in numeric_cols}
        stats = df.groupby(groupby_col, dropna=False).agg(agg_spec)

    # Nice rounding where possible
    stats = stats.round(decimals)

    # Replace NaNs in std on singletons, etc.
    return stats.fillna(np.nan)


# -----------------------------
# Groupby aggregation helper
# -----------------------------
def groupby_aggregate(
    df: pd.DataFrame,
    by: Union[str, Iterable[str]],
    agg: Optional[Dict[str, Union[str, Iterable[str]]]] = None,
    dropna_groups: bool = False,
) -> pd.DataFrame:
    """Flexible groupby aggregation.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    by : str or list-like
        Column(s) to group by.
    agg : dict, optional
        Mapping of column -> aggregation(s). If None, will aggregate all numeric
        columns with ['count', 'mean', 'std', 'min', 'max'].
    dropna_groups : bool, default=False
        If False, keep NaN keys as a group.

    Returns
    -------
    pd.DataFrame
        Aggregated result.
    """
    if agg is None:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        agg = {col: ["count", "mean", "std", "min", "max"] for col in numeric_cols}
    return df.groupby(by, dropna=dropna_groups).agg(agg)


# -----------------------------
# Plotting helpers
# -----------------------------
def basic_histogram(
    df: pd.DataFrame,
    column: str,
    bins: int = 30,
    figsize: Tuple[int, int] = (6, 4),
    title: Optional[str] = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """Create a simple histogram for a numeric column.

    Returns the (fig, ax) so caller can further customize or save.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not in DataFrame.")
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(df[column].dropna(), bins=bins)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.set_title(title or f"Histogram of {column}")
    fig.tight_layout()
    return fig, ax


def save_plot(fig: plt.Figure, path: Union[str, Path], dpi: int = 120) -> Path:
    """Save a Matplotlib figure, creating parent directories if needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    return path
