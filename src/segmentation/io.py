from __future__ import annotations
from pathlib import Path
import pandas as pd

def load_csv(path: str | Path) -> pd.DataFrame:
    """
    Load a CSV with helpful validation and light cleanup.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the CSV cannot be read or is empty / has no usable columns.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"CSV not found: {p}")

    try:
        df = pd.read_csv(p)
    except Exception as e:
        raise ValueError(f"Failed to read CSV {p}: {e}") from e

    if df.empty:
        raise ValueError("CSV is empty")

    # Drop index-like columns commonly named 'Unnamed: 0', etc.
    df = df.loc[:, ~df.columns.str.contains(r"^Unnamed")]

    if df.shape[1] == 0:
        raise ValueError("CSV has no usable columns after cleanup")

    return df
