#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))  # add ../src to path
from logger_utils import get_logger, touch_ok  # type: ignore

def compute_rolling_corr(df: pd.DataFrame, eq_col: str, bond_col: str, window: int) -> pd.DataFrame:
    if eq_col not in df.columns or bond_col not in df.columns:
        raise ValueError(f"Missing columns: need '{eq_col}' and '{bond_col}'. Found: {list(df.columns)}")
    # Ensure sorted by date index
    if not isinstance(df.index, pd.DatetimeIndex):
        # try to parse a column named 'date'
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            df = df.set_index('date')
        else:
            raise ValueError("DataFrame must have a DatetimeIndex or a 'date' column.")
    df = df.sort_index()
    # compute log returns for robustness
    returns = np.log(df[[eq_col, bond_col]].astype(float)).diff()
    corr = returns[eq_col].rolling(window).corr(returns[bond_col])
    out = pd.DataFrame({"rolling_corr": corr}).dropna()
    return out

def main():
    p = argparse.ArgumentParser(description="Compute rolling correlation between equity and bond price series.")
    p.add_argument("--prices", type=Path, required=True, help="Input file (.csv or .parquet) with dates + price columns")
    p.add_argument("--eq-col", type=str, required=True, help="Equity column name (e.g., SPY)")
    p.add_argument("--bond-col", type=str, required=True, help="Bond column name (e.g., TLT)")
    p.add_argument("--window", type=int, default=60, help="Rolling window size (days)")
    p.add_argument("--out", type=Path, required=True, help="Output CSV path")
    p.add_argument("--logdir", type=Path, default=Path(__file__).resolve().parents[1] / "logs", help="Logs directory")
    args = p.parse_args()

    logger = get_logger("rolling_corr", args.logdir)
    logger.info(f"Start: prices={args.prices}, eq={args.eq_col}, bond={args.bond_col}, window={args.window}")

    if not args.prices.exists():
        logger.error(f"Input file not found: {args.prices}")
        sys.exit(2)

    # Load
    ext = args.prices.suffix.lower()
    if ext == ".csv":
        df = pd.read_csv(args.prices)
    elif ext == ".parquet":
        df = pd.read_parquet(args.prices)
    else:
        logger.error("Unsupported input format. Use .csv or .parquet")
        sys.exit(2)

    try:
        out = compute_rolling_corr(df, args.eq_col, args.bond_col, args.window)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(args.out, index=True)
        touch_ok(args.out.with_suffix(".ok"))
        logger.info(f"SUCCESS: wrote {len(out):,} rows to {args.out}")
    except Exception as e:
        logger.exception(f"FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
