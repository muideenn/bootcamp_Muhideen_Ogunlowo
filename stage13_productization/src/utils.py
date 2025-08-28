
from pathlib import Path
import pandas as pd
import pickle

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def project_path(*parts) -> Path:
    """Return absolute path under the repo root."""
    return PROJECT_ROOT.joinpath(*parts)

def save_df(df: pd.DataFrame, rel_path: str) -> Path:
    p = project_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return p

def load_csv(rel_path: str) -> pd.DataFrame:
    p = project_path(rel_path)
    return pd.read_csv(p)

def save_model(model, rel_path: str = "model/model.pkl") -> Path:
    p = project_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "wb") as f:
        pickle.dump(model, f)
    return p

def load_model(rel_path: str = "model/model.pkl"):
    p = project_path(rel_path)
    with open(p, "rb") as f:
        return pickle.load(f)
