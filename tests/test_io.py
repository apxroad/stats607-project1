import pandas as pd
import pytest
from pathlib import Path
from segmentation.io import load_csv

def test_load_csv_success(tmp_path: Path):
    csv = tmp_path / "tiny.csv"
    pd.DataFrame({"a": [1, 2, 3], "b": [4.0, 5.0, 6.0], "txt": ["x", "y", "z"]}).to_csv(csv, index=False)
    df = load_csv(csv)
    assert df.shape == (3, 3)
    assert list(df.columns) == ["a", "b", "txt"]

def test_load_csv_missing_file(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_csv(tmp_path / "nope.csv")

