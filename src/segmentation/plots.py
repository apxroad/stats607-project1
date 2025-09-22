from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

def save_elbow(df_scores: pd.DataFrame, outdir: str | Path) -> Path:
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots()
    ax.plot(df_scores.index, df_scores["inertia"], marker="o")
    ax.set_xlabel("k"); ax.set_ylabel("inertia"); ax.set_title("Elbow plot")
    p = out / "elbow.png"
    fig.savefig(p, bbox_inches="tight"); plt.close(fig)
    return p

def save_silhouette(df_scores: pd.DataFrame, outdir: str | Path) -> Path:
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots()
    ax.plot(df_scores.index, df_scores["silhouette"], marker="o")
    ax.set_xlabel("k"); ax.set_ylabel("avg silhouette"); ax.set_title("Silhouette vs k")
    p = out / "silhouette.png"
    fig.savefig(p, bbox_inches="tight"); plt.close(fig)
    return p

def save_pca_scatter(X: pd.DataFrame, labels, outdir: str | Path) -> Path:
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    pca = PCA(n_components=2, random_state=0)
    Z = pca.fit_transform(X)
    fig, ax = plt.subplots()
    ax.scatter(Z[:,0], Z[:,1], c=labels, s=12, cmap="tab10")
    ax.set_xlabel("PC1"); ax.set_ylabel("PC2"); ax.set_title("PCA scatter (by cluster)")
    p = out / "pca_scatter.png"
    fig.savefig(p, bbox_inches="tight"); plt.close(fig)
    return p
