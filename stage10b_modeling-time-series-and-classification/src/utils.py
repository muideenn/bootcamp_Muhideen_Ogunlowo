
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def project_path(*parts) -> Path:
    return Path(__file__).resolve().parents[1].joinpath(*parts)

def save_df(df: pd.DataFrame, rel_path: str) -> Path:
    p = project_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=True)
    return p

def classification_report_df(y_true, y_pred) -> pd.DataFrame:
    return pd.DataFrame({
        "accuracy":[accuracy_score(y_true, y_pred)],
        "precision":[precision_score(y_true, y_pred, zero_division=0)],
        "recall":[recall_score(y_true, y_pred, zero_division=0)],
        "f1":[f1_score(y_true, y_pred, zero_division=0)]
    })

def plot_confusion_matrix(y_true, y_pred, ax=None, title="Confusion Matrix"):
    import numpy as np
    cm = confusion_matrix(y_true, y_pred)
    if ax is None:
        fig, ax = plt.subplots(figsize=(4,4))
    im = ax.imshow(cm, interpolation='nearest')
    ax.set_title(title)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_xticks([0,1]); ax.set_yticks([0,1])
    for (i, j), val in np.ndenumerate(cm):
        ax.text(j, i, int(val), ha='center', va='center')
    return ax

