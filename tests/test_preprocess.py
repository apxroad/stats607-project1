import numpy as np
import pandas as pd
import pytest
from segmentation.preprocess import standardize

def test_standardize_numeric_only():
    df = pd.DataFrame({"a":[1,2,3], "b":[10.0, 11.0, 12.0], "c":["x","y","z"]})
    X, scaler = standardize(df)
    assert list(X.columns) == ["a", "b"]
    # means ~ 0
    assert np.allclose(X.mean().values, 0.0, atol=1e-7)
    # std ~ 1
    assert np.allclose(X.std(ddof=0).values, 1.0, atol=1e-6)

def test_standardize_no_numeric():
    df = pd.DataFrame({"c":["x","y","z"]})
    with pytest.raises(ValueError):
        standardize(df)

