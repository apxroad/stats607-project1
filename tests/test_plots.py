from pathlib import Path
import numpy as np
import pandas as pd
from segmentation.plots import save_elbow, save_silhouette, save_pca_scatter

def _dummy_scores():
    return pd.DataFrame({"inertia":[100,80,70], "silhouette":[0.2,0.3,0.25]}, index=[2,3,4])

def test_save_elbow_and_silhouette(tmp_path: Path):
    scores = _dummy_scores()
    p1 = save_elbow(scores, tmp_path)
    p2 = save_silhouette(scores, tmp_path)
    assert Path(p1).exists()
    assert Path(p2).exists()

def test_save_pca_scatter(tmp_path: Path):
    X = pd.DataFrame({"a": np.random.randn(12), "b": np.random.randn(12)})
    labels = [0,0,0,0,1,1,1,1,2,2,2,2]
    p = save_pca_scatter(X, labels, tmp_path)
    assert Path(p).exists()

