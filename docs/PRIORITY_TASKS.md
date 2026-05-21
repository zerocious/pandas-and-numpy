# Tasks by priority

## A. Portfolio & repo (employer-facing)

| Priority | Task | Status |
|:--------:|------|:------:|
| **P1** | Portfolio [README.md](../README.md) + project map | ✅ |
| **P2** | GitHub Actions CI + badge | ✅ |
| **P2** | MIT [LICENSE](../LICENSE) | ✅ |
| **P3** | [data/README.md](../data/README.md) data dictionary | ✅ |
| **P3** | All raw CSVs + tests pass | ✅ |
| **P4** | [HINTS.en.md](../notes/HINTS.en.md) / [HINTS.ru.md](../notes/HINTS.ru.md) | ✅ |
| **P4** | Bilingual [00-index.ipynb](../notebooks/00-index.ipynb) | ✅ |
| **P5** | [SHOWCASE.md](SHOWCASE.md) | ✅ |
| **P5** | [samples/](samples/) example rows | ✅ |
| **P6** | Draft notes removed / gitignored | ✅ |
| **P6** | [mistakes.md](../notes/mistakes.md) learning takeaways | ✅ |
| **P6** | Pin repo — [GITHUB_PROFILE.md](GITHUB_PROFILE.md) (manual step) | 📌 you |
| **P7** | [pyproject.toml](../pyproject.toml) | ✅ |
| **P7** | GitHub repo description | ✅ |
| **P7** | [scripts/README.md](../scripts/README.md) | ✅ |

---

## B. Learning exercises (study order)

| Priority | Task | Notebook | Check when done |
|:--------:|------|----------|-----------------|
| **P1** | Users + orders → regional metrics | [03](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | `metrics_by_region.csv` |
| **P1** | Cleaning pipeline | [02 §5.3](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | `clean_orders.csv` |
| **P1** | GroupBy + transform | [02 §6](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | exercises run |
| **P2** | Cohort retention | [03](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | `cohort_retention_real.csv` |
| **P2** | Merge + pivot / melt | [02 §7](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | exercises run |
| **P2** | Customer 360 | [04](../notebooks/ru/04-pandas-business-tasks.ipynb) | `customer_master.csv` |
| **P3–P5** | Remaining pipelines & NumPy | see [PROGRESS.md](../notes/PROGRESS.md) | |

Hints: [HINTS.en.md](../notes/HINTS.en.md) · [HINTS.ru.md](../notes/HINTS.ru.md)

```bash
pytest
python scripts/run_solution_notebooks.py
```
