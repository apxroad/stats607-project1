# Project 1 — Reproducible KMeans Segmentation

This project refactors the original notebook (`Assignment_2_Kmeans/210266_assignment2_notebook.ipynb`)
into a clear, **installable**, **tested**, and **one-command** pipeline that reproduces the same results
(figures, a metrics table, and simple metadata).

**Goal:** frictionless reproducibility — clone, install, run one command, get the same outputs.

---

## What’s in this repo

- `Assignment_2_Kmeans/` — original notebook (reference only)
- `data/` — input data (e.g., `credit-card-holder-data.csv`) **included**
- `src/segmentation/` — library code
  - `io.py` (load CSV)
  - `preprocess.py` (scale numeric columns)
  - `model.py` (KMeans + sweep over k)
  - `plots.py` (elbow, silhouette, PCA scatter)
  - `run_pipeline.py` (main pipeline)
- `run_analysis.py` — one-command wrapper required by the assignment
- `tests/` — pytest tests (unit + end-to-end)
- `artifacts/` — outputs (images, CSV, metadata) **ignored by git**
- `requirements.txt` — dependencies
- `pyproject.toml` — packaging and console script
- `README.md` — this file
- `Unit 1 Project - Frictionless Reproducibility (due by 11pm on 9-23).pdf` — assignment brief

---

## Environment & install

> Python 3.10+ recommended.

```bash
# from project root
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
