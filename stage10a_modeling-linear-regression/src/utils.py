from pathlib import Path
import pandas as pd

def project_path(*parts) -> Path:
    """Return absolute path inside the project (relative to this file's parent parent)."""
    here = Path(__file__).resolve()
    root = here.parent.parent
    return root.joinpath(*parts)

def save_df(df: pd.DataFrame, rel_path: str | Path) -> Path:
    p = project_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return p

def load_csv(rel_path: str | Path) -> pd.DataFrame:
    p = project_path(rel_path)
    return pd.read_csv(p)
