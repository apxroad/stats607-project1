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
  - `io.py` — load CSV with simple validation  
  - `preprocess.py` — scale numeric columns (StandardScaler)  
  - `model.py` — KMeans fit + sweep over k  
  - `plots.py` — elbow, silhouette, PCA scatter  
  - `run_pipeline.py` — main pipeline (argument parser)
- `run_analysis.py` — one-command wrapper (runs the full pipeline with defaults)
- `tests/` — pytest tests (unit + end-to-end)
- `artifacts/` — outputs (images, CSV, metadata) **ignored by git**
- `requirements.txt` — dependencies
- `pyproject.toml` — packaging and console script
- `README.md` — this file
- `Unit 1 Project - Frictionless Reproducibility (due by 11pm on 9-23).pdf` — assignment brief

> Note: legacy materials (e.g., `baseline/`, external `Kmeans/`) are **not** tracked in git.

---

## Environment & install

> Python 3.10+ recommended.

~~~bash
# from project root
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
~~~

---

## Run the full pipeline (one command)

Choose either of these:

### Option A: `run_analysis.py`

~~~bash
python run_analysis.py
~~~

### Option B:

~~~bash
segmentation \
  --data data/credit-card-holder-data.csv \
  --k-min 2 --k-max 10 --k 6 \
  --random-state 42 \
  --out artifacts
~~~

*(Windows PowerShell)*

~~~powershell
segmentation --data data\credit-card-holder-data.csv --k-min 2 --k-max 10 --k 6 --random-state 42 --out artifacts
~~~

### Expected outputs (written to `artifacts/`)

- `elbow.png` — inertia vs. k  
- `silhouette.png` — average silhouette vs. k  
- `pca_scatter.png` — 2D PCA of samples colored by cluster  
- `scores.csv` — inertia and silhouette for each k in the sweep  
- `metadata.json` — parameters, timestamp, and git commit

---

## Testing

Run tests inside the virtual environment:

~~~bash
python -m pytest -q
~~~

Covers:
- CSV loading (`io.py`)
- Scaling (`preprocess.py`)
- KMeans fit and k-sweep (`model.py`)
- Plot creation (`plots.py`)
- End-to-end run of the pipeline

---

## Project structure 

```text
.
├── Assignment_2_Kmeans/                  # Original notebook folder (reference only)
│   └── 210266_assignment2_notebook.ipynb # The raw notebook this project refactors
├── data/                                 # Input data used by the pipeline
│   └── credit-card-holder-data.csv       # Customer features for clustering
├── src/                                  # Installable Python package source
│   └── segmentation/                     # Package name: `segmentation`
│       ├── __init__.py                   # Package marker / exports (keeps namespace clean)
│       ├── io.py                         # load_csv(): read CSV with simple validation
│       ├── preprocess.py                 # standardize(): scale numeric columns (StandardScaler)
│       ├── model.py                      # fit_kmeans(), sweep_k(): core KMeans logic + metrics
│       ├── plots.py                      # save_elbow(), save_silhouette(), save_pca_scatter()
│       └── run_pipeline.py               # Orchestrates the full run; CLI args → load → prep → model → plots
├── run_analysis.py                       # One-command wrapper (assignment-friendly entry point)
├── tests/                                # Pytest test suite (unit + end-to-end)
│   ├── test_io.py                        # Validates CSV loading behavior
│   ├── test_preprocess.py                # Checks scaling output and shapes
│   ├── test_model.py                     # Checks labels length, inertia>0, silhouette range, monotonicity
│   ├── test_plots.py                     # Ensures plot files are created
│   └── test_e2e_pipeline.py              # Runs the whole pipeline on the CSV end-to-end
├── artifacts/                            # Runtime outputs (git-ignored)
│   ├── elbow.png                         # Inertia vs k
│   ├── silhouette.png                    # Average silhouette vs k
│   ├── pca_scatter.png                   # 2D PCA of samples colored by cluster
│   ├── scores.csv                        # Inertia & silhouette for each k in the sweep
│   └── metadata.json                     # Parameters, timestamp, git commit
├── requirements.txt                      # Minimal dependencies to reproduce
├── pyproject.toml                        # Package metadata + console_script entrypoint
├── README.md                             # Install / run / test instructions (this file)
├── .gitignore                            # Ignore rules (e.g., venv/, artifacts/, baseline/, Kmeans/)
└── Unit 1 Project - Frictionless Reproducibility (due by 11pm on 9-23).pdf
                                         # The assignment brief


---

## Troubleshooting

- **`python: command not found`** → use `python3` (macOS/Linux).  
- **`segmentation: command not found`** → you likely didn’t run `pip install -e .` inside the venv; activate the venv and reinstall.  
- **Tests say `No module named numpy/pandas`** → you’re using system Python; run `python -m pytest -q` after activating the venv.  
- **`CSV not found`** → check the `--data` path; the repo includes `data/credit-card-holder-data.csv`.  
- **Editable install errors about `*.egg-info`** → clean build artefacts, then reinstall:
  ~~~bash
  rm -rf build/ dist/ *.egg-info
  find . -name "*.egg-info" -type d -exec rm -rf {} +
  pip install -e .
  ~~~

---

