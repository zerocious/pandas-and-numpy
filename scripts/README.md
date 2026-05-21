# Maintainer scripts

Utilities for regenerating notebooks and outputs. Not required for reviewers running the portfolio.

| Script | Purpose |
|--------|---------|
| `run_solution_notebooks.py` | Execute all solution notebooks → `data/output/` |
| `build_lang_task_notebooks.py` | Regenerate aligned `notebooks/ru/` and `notebooks/en/` task notebooks |
| `task_notebook_content.py` | RU/EN task text consumed by the builder (edit here, then rebuild) |
| `clear_notebook_outputs.py` | Strip execution outputs before git commit |
| `split_notebooks.py` | Split monolithic notebook into topic parts |
| `convert_tasks_markdown.py` | Convert task comment cells to markdown |
| `fix_solution_quality.py` | Apply code-style fixes to solution notebooks |
| `fix_csv_paths.py` | Normalize `to_csv` paths to `OUT` helper |

```bash
python scripts/run_solution_notebooks.py
python scripts/clear_notebook_outputs.py
```
