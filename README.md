# Pandas and NumPy

Practice notebooks and datasets for NumPy and pandas exercises.

## Project layout

```
pandas-and-numpy/
├── notebooks/
│   ├── 00-index.ipynb              # Start here
│   ├── 01-numpy.ipynb … 04-pandas-business.ipynb   # Solutions
│   ├── ru/                         # Task notebooks (Russian)
│   └── en/                         # Task notebooks (English)
├── data/
│   ├── raw/                        # Input CSVs (committed)
│   └── output/                     # Generated exports (gitignored)
├── notes/
│   ├── HINTS.md                    # Hints if you're stuck
│   ├── PROGRESS.md                 # Section checklist
│   └── mistakes.md                 # Your mistake log
├── tests/
├── scripts/
├── README.md
└── requirements.txt
```

> **Translation disclaimer:** Task notebooks in `notebooks/ru/` and `notebooks/en/` were translated by the repository author using AI (Cursor AI). They are not professional translations.

## How to study

1. Open **`notebooks/00-index.ipynb`**.
2. Pick a language folder: [`notebooks/ru/`](notebooks/ru/) or [`notebooks/en/`](notebooks/en/).
3. Work through `*-tasks.ipynb` files; write code under `# Your solution here` / `# Ваше решение здесь`.
4. Compare with the matching solution notebook in `notebooks/`.
5. Track progress in [`notes/PROGRESS.md`](notes/PROGRESS.md).
6. Stuck? [`notes/HINTS.md`](notes/HINTS.md)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook notebooks/
```

Task notebooks use `ROOT = Path('../..')` so paths work from `notebooks/ru/` or `notebooks/en/`.

## Verify your work

```bash
pytest
python scripts/run_solution_notebooks.py
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/build_lang_task_notebooks.py` | Regenerate `ru/` and `en/` task notebooks |
| `scripts/run_solution_notebooks.py` | Execute all solution notebooks |
| `scripts/split_notebooks.py` | Re-split monolithic notebook (maintenance) |

## License

MIT — see [LICENSE](LICENSE).

## Requirements

- Python 3.10+
- See `requirements.txt`
