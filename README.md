# Pandas analytics portfolio

End-to-end **NumPy & pandas** lab: dirty CSV ingestion, merges, cohort retention, sessionization, and BI-ready exports.

![CI](https://github.com/zerocious/pandas-and-numpy/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Author:** [@zerocious](https://github.com/zerocious)

## Skills demonstrated

- Vectorized **NumPy** (broadcasting, masks, performance vs loops)
- **pandas** cleaning: dtypes, `DD.MM.YYYY` parsing, deduplication, imputation
- **merge** with `validate`, **groupby** / **transform** / named **agg**
- **melt** & **pivot_table** for wide → long → analytic matrices
- Cohort **retention** and revenue dashboards
- Event **sessionization** (`diff`, `cumsum`, `Timedelta`)
- Channel **concentration** (HHI, share metrics)

## Project map

| Notebook | Business problem | Key output |
|----------|------------------|------------|
| [01-numpy](notebooks/01-numpy.ipynb) | Array ops, normalization, vector pipelines | In-notebook |
| [02-pandas-fundamentals](notebooks/02-pandas-fundamentals.ipynb) | DataFrame basics, groupby, merge/melt/pivot | `clean_orders.csv` |
| [03-pandas-pipelines](notebooks/03-pandas-pipelines.ipynb) | Users×orders metrics, cohorts, events | `metrics_by_region.csv`, `cohort_retention_real.csv`, … |
| [04-pandas-business](notebooks/04-pandas-business.ipynb) | Customer 360, churn risk, channel concentration | `customer_master.csv`, `churn_risk_analysis.csv`, … |

Case studies: [docs/SHOWCASE.md](docs/SHOWCASE.md) · Data dictionary: [data/README.md](data/README.md)

## Quick start

```bash
git clone https://github.com/zerocious/pandas-and-numpy.git
cd pandas-and-numpy
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
pytest
jupyter notebook notebooks/00-index.ipynb
```

## Task notebooks (RU / EN)

| Language | Folder |
|----------|--------|
| Русский | [notebooks/ru/](notebooks/ru/) |
| English | [notebooks/en/](notebooks/en/) |

Hints: [notes/HINTS.en.md](notes/HINTS.en.md) · [notes/HINTS.ru.md](notes/HINTS.ru.md)

Task texts in `ru/` and `en/` were translated by the author with AI assistance (not professional translations). **Solution code** in the main notebooks is the primary portfolio artifact.

## Repository layout

```
notebooks/     # Solutions + ru/ + en/ tasks
data/raw/      # Input CSVs
data/output/   # Generated exports (gitignored)
tests/         # pytest checks on raw data & outputs
docs/          # SHOWCASE, samples, priority tasks
```

## Verify

```bash
pytest
python scripts/run_solution_notebooks.py   # optional: regenerate outputs
```

Maintainer scripts: [scripts/README.md](scripts/README.md)

## Links

- [Progress checklist](notes/PROGRESS.md)
- [Priority tasks](docs/PRIORITY_TASKS.md)
- [Learning takeaways](notes/mistakes.md)
- [Pin this repo on GitHub](docs/GITHUB_PROFILE.md)

## License

MIT — see [LICENSE](LICENSE).
