from pathlib import Path
import logging
from datetime import datetime

def get_logger(name: str, log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # Avoid duplicate handlers during repeated imports
    if not logger.handlers:
        fh = logging.FileHandler(log_dir / f"{name}.log")
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger

def touch_ok(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
