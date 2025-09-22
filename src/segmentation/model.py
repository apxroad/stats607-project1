from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

@dataclass
class KMeansResult:
    labels_: np.ndarray
    inertia_: float
    silhouette_: float | None

def fit_kmeans(
    X: pd.DataFrame,
    k: int,
    random_state: int = 42,
    n_init: int = 10
) -> KMeansResult:
    """
    Fit KMeans and compute labels, inertia, and silhouette (if >1 cluster present).
    """
    if k < 2:
        raise ValueError("k must be >= 2")
    if X.shape[0] < k:
        raise ValueError(f"n_samples ({X.shape[0]}) must be >= k ({k})")

    km = KMeans(n_clusters=k, random_state=random_state, n_init=n_init)
    labels = km.fit_predict(X)
    sil = silhouette_score(X, labels) if len(np.unique(labels)) > 1 else None
    return KMeansResult(labels_=labels, inertia_=km.inertia_, silhouette_=sil)

def sweep_k(
    X: pd.DataFrame,
    k_values: Iterable[int],
    random_state: int = 42,
    n_init: int = 10
) -> pd.DataFrame:
    """
    Run KMeans for each k and collect metrics.
    Returns DataFrame indexed by k with columns ['inertia','silhouette'].
    """
    rows = []
    for k in k_values:
        res = fit_kmeans(X, k, random_state=random_state, n_init=n_init)
        rows.append({"k": k, "inertia": res.inertia_, "silhouette": res.silhouette_})
    return pd.DataFrame(rows).set_index("k").sort_index()
