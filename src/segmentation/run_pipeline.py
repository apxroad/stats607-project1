from __future__ import annotations
import argparse, json
from pathlib import Path
from datetime import datetime
import subprocess

from segmentation.io import load_csv
from segmentation.preprocess import standardize
from segmentation.model import sweep_k, fit_kmeans
from segmentation.plots import save_elbow, save_silhouette, save_pca_scatter


def main():
    parser = argparse.ArgumentParser(description="Run KMeans clustering pipeline")
    parser.add_argument("--data", type=str, required=True, help="Path to input CSV")
    parser.add_argument("--k-min", type=int, default=2, help="Minimum k for sweep")
    parser.add_argument("--k-max", type=int, default=10, help="Maximum k for sweep")
    parser.add_argument("--k", type=int, default=6, help="Final k for clustering")
    parser.add_argument("--random-state", type=int, default=42, help="Random seed")
    parser.add_argument("--out", type=str, default="artifacts", help="Output directory")
    args = parser.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    # 1. Load data
    df = load_csv(args.data)
    print(f"Loaded {df.shape}")

    # 2. Standardize features
    X_std, scaler = standardize(df)
    print("Standardized features")

    # 3. Sweep k
    df_scores = sweep_k(X_std, range(args.k_min, args.k_max + 1), random_state=args.random_state)
    df_scores.to_csv(outdir / "scores.csv")
    save_elbow(df_scores, outdir)
    save_silhouette(df_scores, outdir)
    print("Saved clustering sweep results")

    # 4. Final fit & PCA scatter
    res = fit_kmeans(X_std, args.k, random_state=args.random_state)
    save_pca_scatter(X_std, res.labels_, outdir)
    print(f"Final clustering with k={args.k} saved")

    # 5. Save metadata
    metadata = {
        "data": args.data,
        "k_min": args.k_min,
        "k_max": args.k_max,
        "final_k": args.k,
        "random_state": args.random_state,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }
    # try to record git commit hash
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        metadata["git_commit"] = commit
    except Exception:
        metadata["git_commit"] = None

    with open(outdir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Pipeline finished. Results saved to {outdir}")


if __name__ == "__main__":
    main()