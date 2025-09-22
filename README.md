# Project 1 — Reproducible KMeans Segmentation

This project refactors the original notebook (`Assignment_2_Kmeans/210266_assignment2_notebook.ipynb`)
into a clean, **installable**, **tested**, and **one-command** pipeline that reproduces results
(figures + tables + metadata).

**Key idea:** frictionless reproducibility — clone, install, run one command, get the results.

---

## 📦 What’s in this repo

- `Assignment_2_Kmeans/` — the original notebook (reference only)
- `src/segmentation/` — library code (I/O, preprocessing, modeling, plotting, CLI)
- `tests/` — automated tests (pytest)
- `data/` — local data (e.g., `credit-card-holder-data.csv`)
- `artifacts/` — outputs (plots, tables, metadata) **not tracked in git**
- `requirements.txt` — minimal dependencies
- `pyproject.toml` — packaging & CLI entrypoint
- `README.md` — this document
- `Unit 1 Project - Frictionless Reproducibility (due by 11pm on 9-23).pdf` — assignment

---

## ⚙️ Environment & Installation

```bash
# from project root
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -e .
> Tip: use `python -m pytest -q` to force the venv interpreter.

### Expected outputs
Running the command writes to `artifacts/`:
- `elbow.png`, `silhouette.png`, `pca_scatter.png`
- `scores.csv` (inertia & average silhouette by k)
- `metadata.json` (parameters, timestamp, git commit)

