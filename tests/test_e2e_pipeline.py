import sys
from pathlib import Path
import json
import numpy as np
import pandas as pd
from segmentation.run_pipeline import main as run_main
import pytest

def test_e2e_pipeline_small(tmp_path: Path, monkeypatch):
    # create small synthetic dataset
    rng = np.random.default_rng(0)
    X = pd.DataFrame({
        "a": rng.normal(size=60),
        "b": rng.normal(size=60),
        "c": rng.normal(size=60),
    })
    csv_path = tmp_path / "tiny.csv"
    X.to_csv(csv_path, index=False)

    outdir = tmp_path / "artifacts"
    args = [
        "segmentation.run_pipeline",  # program name placeholder
        "--data", str(csv_path),
        "--k-min", "2",
        "--k-max", "5",
        "--k", "3",
        "--random-state", "0",
        "--out", str(outdir),
    ]
    monkeypatch.setattr(sys, "argv", args)
    run_main()  # run the CLI's main()

    # verify outputs
    assert (outdir / "scores.csv").exists()
    assert (outdir / "elbow.png").exists()
    assert (outdir / "silhouette.png").exists()
    assert (outdir / "pca_scatter.png").exists()
    meta = json.loads((outdir / "metadata.json").read_text())
    for key in ["data","k_min","k_max","final_k","random_state","timestamp"]:
        assert key in meta

