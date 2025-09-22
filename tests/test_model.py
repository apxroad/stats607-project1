import numpy as np
import pandas as pd
import pytest
from segmentation.model import fit_kmeans, sweep_k, KMeansResult

def test_fit_kmeans_basic():
    # two easy clusters
    X = pd.DataFrame({"x": [0,0,1,1,10,10,11,11]})
    res = fit_kmeans(X, k=2, random_state=0)
    assert isinstance(res, KMeansResult)
    assert len(res.labels_) == len(X)
    assert res.inertia_ >= 0
    # silhouette can be None only if one cluster; here k=2 -> should be numeric
    assert res.silhouette_ is not None
    assert -1.0 <= res.silhouette_ <= 1.0

def test_fit_kmeans_invalid_k():
    X = pd.DataFrame({"x": np.arange(5)})
    with pytest.raises(ValueError):
        fit_kmeans(X, k=1)
    with pytest.raises(ValueError):
        fit_kmeans(X, k=10)

def test_sweep_k_monotonic_inertia():
    rng = np.random.default_rng(0)
    X = pd.DataFrame(rng.normal(size=(60, 3)), columns=["a","b","c"])
    scores = sweep_k(X, range(2, 7), random_state=0)
    inertias = scores["inertia"].tolist()
    # inertia should be non-increasing as k grows
    assert all(x >= y - 1e-8 for x, y in zip(inertias, inertias[1:]))

