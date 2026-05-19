# Pandas and NumPy

Practice notebooks and datasets for NumPy and pandas exercises.

## Project layout

```
pandas-and-numpy/
├── notebooks/
│   ├── 00-index.ipynb              # Start here
│   ├── 01-numpy.ipynb / 01-numpy-tasks.ipynb
│   ├── 02-pandas-fundamentals.ipynb / …-tasks.ipynb
│   ├── 03-pandas-pipelines.ipynb / …-tasks.ipynb
│   └── 04-pandas-business.ipynb / …-tasks.ipynb
├── data/
│   ├── raw/                        # Input CSVs (committed)
│   └── output/                     # Generated exports (gitignored)
├── notes/
│   ├── HINTS.md                    # Hints if you're stuck (per task)
│   ├── PROGRESS.md                 # Section checklist
│   └── mistakes.md                 # Your mistake log
├── tests/                          # pytest checks
├── scripts/                        # Repo utilities
├── README.md
└── requirements.txt
```

## How to study

1. Open **`notebooks/00-index.ipynb`** or a `*-tasks.ipynb` notebook.
2. Read each task in the **markdown** cells; write code under `# Your solution here`.
3. Compare with the matching solution notebook (same number, without `-tasks`).
4. Track progress in [`notes/PROGRESS.md`](notes/PROGRESS.md).
5. Stuck? Read hints for that task in [`notes/HINTS.md`](notes/HINTS.md) — nudges only, not full answers.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
jupyter notebook notebooks/
```

Paths assume notebooks run from the `notebooks/` folder. Each notebook defines `RAW` and `OUT` for data paths.

## Verify your work

After solving pipeline/business tasks (or running solution notebooks):

```bash
pytest
```

Skipped tests mean the matching file in `data/output/` is missing — run your code or:

```bash
python scripts/run_solution_notebooks.py
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run_solution_notebooks.py` | Execute all solution notebooks |
| `scripts/split_notebooks.py` | Re-split monolithic notebook (maintenance) |
| `scripts/convert_tasks_markdown.py` | Regenerate markdown task cells |
| `scripts/fix_solution_quality.py` | Apply code-style fixes to solutions |

## Requirements

- Python 3.10+
- Pinned in `requirements.txt`: numpy, pandas, jupyter, pytest
