from pathlib import Path
import pandas as pd

def project_path(*parts) -> Path:
    return Path(__file__).resolve().parents[1].joinpath(*parts)

def save_df(df: pd.DataFrame, rel_path: str) -> Path:
    p = project_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return p

def load_csv(rel_path: str) -> pd.DataFrame:
    return pd.read_csv(project_path(rel_path))
