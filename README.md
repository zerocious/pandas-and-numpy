# Pandas and NumPy

Practice notebooks and datasets for NumPy and pandas exercises.

## Project layout

```
pandas-and-numpy/
├── notebooks/
│   ├── 00-index.ipynb              # Start here — links to all parts
│   ├── 01-numpy.ipynb              # Solutions
│   ├── 01-numpy-tasks.ipynb        # Tasks only
│   ├── 02-pandas-fundamentals.ipynb
│   ├── 02-pandas-fundamentals-tasks.ipynb
│   ├── 03-pandas-pipelines.ipynb
│   ├── 03-pandas-pipelines-tasks.ipynb
│   ├── 04-pandas-business.ipynb
│   └── 04-pandas-business-tasks.ipynb
├── data/
│   ├── raw/                        # Input CSV files (committed)
│   └── output/                     # Generated exports (not committed)
├── notes/                          # Study notes
├── scripts/                        # Repo utilities
├── README.md
└── requirements.txt
```

## How to study

1. Open **`notebooks/00-index.ipynb`** or jump straight to a `*-tasks.ipynb` notebook.
2. Solve each exercise below the `# Your solution here` marker.
3. Compare your work with the matching solution notebook (same number, without `-tasks`).
4. Re-run solution cells if you need to regenerate files in `data/output/`.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook notebooks/
```

Paths in notebooks assume you run them from the `notebooks/` folder. A setup cell at the top defines `RAW` and `OUT` for data paths.

## Requirements

- Python 3.10+
- See pinned versions in `requirements.txt`
