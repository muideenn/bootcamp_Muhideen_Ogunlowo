
from __future__ import annotations
import pandas as pd

def non_empty(df: pd.DataFrame) -> None:
    assert len(df) > 0, "DataFrame is empty"
