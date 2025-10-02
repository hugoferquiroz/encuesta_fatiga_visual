<!-- Auto-generated: guidance for AI coding agents working on this repo -->
# Copilot instructions for the encuesta_fatiga_visual project

This repository contains materials and data for an application and analysis of the CVS‑Q (computer vision syndrome) survey. The codebase is small and currently contains a README and a `data/` folder with the survey datasets. Use these instructions to be productive when making changes or adding analysis code.

Key files and folders
- `Readme.md` — describes the instrument, scoring (Severidad = Frecuencia × Intensidad), interpretation thresholds (SVI ≥ 6) and common analyses.
- `data/` — contains the raw datasets used for analysis (for example `Base de datos UPAO.xlsx` and `BASE DE DATOS UPAO FINAL TODO.sav`).

Quick overview / big picture
- Purpose: convert survey responses into numeric severity scores per the README (item score = frequency × intensity), compute total scores and classify participants (SVI if total ≥ 6; severity buckets: 6–10, 11–20, >20). Most future work will add analysis scripts (Python/R) that load files from `data/`, implement scoring, and produce summary tables and figures.
- Boundaries: this repository stores data and documentation. There is no existing code, tests, or build system in the repo root. New analysis code should live under a top-level `src/` or `analysis/` folder and be self-contained (requirements in `requirements.txt` or `pyproject.toml`).

Project-specific patterns and conventions discovered
- Data-first project: raw datasets in `data/` are the source of truth. Always work on copies and add any derived datasets to `data/derived/` or `output/` to avoid overwriting original files.
- Single authoritative README: domain rules (score calculation and thresholds) live in `Readme.md` — reference it in any analysis scripts and unit tests.
- Prefer explicit scoring implementation: implement the severity calculation as a small, well-documented function (example name: `compute_severity(frequency, intensity)`) and a wrapper `score_responses(df)` that returns item-level and total scores.

When you add code, follow these practices
- Project layout suggestion (recommended):
  - `src/` or `analysis/` — scripts and modules (e.g., `score.py`, `summaries.py`, `plots.py`)
  - `requirements.txt` — pinned dependencies (if using Python)
  - `data/derived/` or `output/` — derived CSVs, figures, notebooks
  - `tests/` — minimal unit tests for scoring and parsing
- Data loading: support both `.xlsx` and `.sav` input. For Python, prefer `pandas.read_excel` and `pyreadstat.read_sav` (or `read_spss` from `pyreadstat`).
- Scoring function contract (use in tests and code):
  - Input: frequency ∈ {0,1,2}, intensity ∈ {0,1,2}
  - Output: severity ∈ {0,1,2,4} computed as frequency * intensity
  - Edge rule: if frequency == 0, force intensity to 0 (README rule)

Examples from this repo
- The README documents exact thresholds and scoring rules — cite `Readme.md` in docstrings and tests. When adding tests, assert that an all-zero frequency/intensity vector produces total 0 and that a canonical sample with scores summing to 6 is classified as SVI.

Developer workflows (what to run locally)
- There is no existing build script. For Python workflows, use a virtual environment then install dependencies and run scripts or tests. Example (PowerShell):

```powershell
# create venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/score.py --input data/"Base de datos UPAO.xlsx" --output data/derived/scores.csv
pytest -q
```

Integration points and external dependencies
- External files: `data/*.xlsx` and `data/*.sav` are required to reproduce analyses. Avoid checking sensitive or private data into source control; if you add processing scripts, make them robust to missing or partial files and provide a small sample dataset for CI.
- If using SPSS `.sav` files, prefer `pyreadstat` for Python; document this in `requirements.txt`.

What to avoid / repo-specific gotchas
- Do not modify original files in `data/`. Add derived outputs under `data/derived/`.
- The README contains the authoritative scoring rules; do not hard-code different thresholds without documenting why.
- There is no CI configured; if you add CI, include a lightweight dataset or mock to keep tests fast.

If you change or add files
- Update this `.github/copilot-instructions.md` with any new conventions or workflows.
- Add a `README` in any new top-level folder (`src/`, `analysis/`, `tests/`) describing how to run the code inside it.

Questions for the repository owner
- Do you want a preferred language for analysis code (Python or R)?
- Should derived datasets be committed, or kept out of version control and only stored in `data/derived/` locally?

If something here looks wrong or incomplete, point to the file(s) and I'll update this guidance.
