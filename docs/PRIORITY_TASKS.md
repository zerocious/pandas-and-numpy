# Tasks by priority

Two tables: **repo improvements** (for employers / GitHub) and **learning exercises** (what to solve first).

---

## A. Portfolio & repo (employer-facing)

| Priority | Task | Why | Status |
|:--------:|------|-----|:------:|
| **P1** | Rewrite [README.md](../README.md) — title, skills, project map, quick start (not “practice exercises” first) | First thing employers read | ⬜ |
| **P1** | Add project map table in README: notebook → business problem → output CSV | Shows impact in 30 seconds | ⬜ |
| **P2** | GitHub Actions CI: `pytest` on every push | Proves repo runs without cloning | ⬜ |
| **P2** | CI badge in README | Visible trust signal | ⬜ |
| **P2** | MIT [LICENSE](../LICENSE) | Clear reuse terms | ✅ |
| **P3** | [data/README.md](../data/README.md) — data dictionary (columns, quirks, year 2023 dates) | Data engineering maturity | ⬜ |
| **P3** | Confirm all raw CSVs present (`user_events.csv`, etc.) + tests pass | Avoid “broken project” | ✅ |
| **P4** | Bilingual hints: `HINTS.en.md` / `HINTS.ru.md` or parallel sections | EN + RU employers | ⬜ |
| **P4** | [00-index.ipynb](../notebooks/00-index.ipynb) — short EN + RU intro | Entry point polish | ⬜ |
| **P5** | [SHOWCASE.md](SHOWCASE.md) — 3 case studies (metrics, cohort, churn) | Explains *your* work | ⬜ |
| **P5** | Optional: `docs/samples/` — one sample row per output | Repo readable without running all notebooks | ⬜ |
| **P6** | Remove or gitignore draft notes (`untitled.md`, `glowing-toasting-flurry.md`) | Cleaner repo | ⬜ |
| **P6** | Expand [mistakes.md](../notes/mistakes.md) into 3–5 learning takeaways | Shows reflection | ⬜ |
| **P6** | Pin repo on GitHub profile; link from profile README | Discoverability | ⬜ |
| **P7** | `pyproject.toml` or Python version badge | Modern Python project look | ⬜ |
| **P7** | Update GitHub repo description (outcome-focused) | Search & profile snippet | ⬜ |
| **P7** | Move maintainer scripts to [scripts/README.md](../scripts/README.md) | README stays employer-focused | ⬜ |

**Suggested order:** P3 → P1 → P2 → P4 → P5 → P6 → P7

---

## B. Learning exercises (study order)

Higher priority = more often asked in analytics / junior data roles.

| Priority | Task | Notebook | Skills | Check when done |
|:--------:|------|----------|--------|-----------------|
| **P1** | Users + orders → regional metrics | [03 pipelines](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | merge, groupby, export | `metrics_by_region.csv` |
| **P1** | Cleaning pipeline (dates, tiers) | [02 fundamentals §5.3](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | datetime, filter, `np.where` | `clean_orders.csv` |
| **P1** | GroupBy + transform | [02 §6.1–6.3](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | agg, transform | exercises run |
| **P2** | Cohort retention | [03 §cohort](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | cohort, retention_rate | `cohort_retention_real.csv` |
| **P2** | Merge + pivot / melt | [02 §7.1–7.3](../notebooks/ru/02-pandas-fundamentals-tasks.ipynb) | merge, melt, pivot | exercises run |
| **P2** | Customer 360 | [04 business §1](../notebooks/ru/04-pandas-business-tasks.ipynb) | merge, fillna, `np.where` | `customer_master.csv` |
| **P3** | Event metrics | [03 events](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | dedupe, median fill, groupby | `event_metrics_2023.csv` |
| **P3** | High-impact quarters | [03 sales_wide](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | melt, pivot | `high_impact_quarters.csv` |
| **P3** | Regional activity | [03 sessions](../notebooks/ru/03-pandas-pipelines-tasks.ipynb) | merge, date diff | `regional_activity.csv` |
| **P4** | Churn / sessions | [04 §2](../notebooks/ru/04-pandas-business-tasks.ipynb) | diff, cumsum, transform | `churn_risk_analysis.csv` |
| **P4** | Channel concentration | [04 §3](../notebooks/ru/04-pandas-business-tasks.ipynb) | melt, HHI, shares | 2 CSV exports |
| **P4** | Regional sales audit | [04 §audit](../notebooks/ru/04-pandas-business-tasks.ipynb) | melt, pivot | audit CSV |
| **P5** | NumPy basics (1.x–2.x) | [01 NumPy](../notebooks/ru/01-numpy-tasks.ipynb) | arrays, masks, broadcasting | all cells |
| **P5** | NumPy vectorization + boss | [01 §3 + boss](../notebooks/ru/01-numpy-tasks.ipynb) | speed, vector ops | boss outputs |

**Paths:** use [notebooks/en/](../notebooks/en/) for English tasks, [notebooks/ru/](../notebooks/ru/) for Russian.

**Hints:** [HINTS.md](../notes/HINTS.md) · **Track progress:** [PROGRESS.md](../notes/PROGRESS.md)

---

## C. Verification (after P1 learning or repo CI)

```bash
pip install -r requirements.txt
pytest
python scripts/run_solution_notebooks.py   # regenerates data/output/
pytest
```
