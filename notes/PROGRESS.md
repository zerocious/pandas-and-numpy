# Progress checklist

**Study order by priority:** [../docs/PRIORITY_TASKS.md](../docs/PRIORITY_TASKS.md) (section B).

Mark sections as you complete them (`[x]`). Compare with the matching `*-tasks.ipynb` / solution notebook pair.

**Stuck on a task?** [HINTS.en.md](HINTS.en.md) · [HINTS.ru.md](HINTS.ru.md) (e.g. [task 1.1](HINTS.en.md#task-11), [pipeline 1](HINTS.en.md#pipeline-1)).

## Notebooks

- [ ] **01 — NumPy** (`ru/01-numpy-tasks.ipynb` or `en/01-numpy-tasks.ipynb`)
  - [ ] 1.1 Arrays & attributes
  - [ ] 1.2 Reshape & views
  - [ ] 1.3 dtype & memory
  - [ ] 2.1 Slicing & masks
  - [ ] 2.2 np.where / select
  - [ ] 2.3 Filtering & segments
  - [ ] 3.1 Broadcasting
  - [ ] 3.2 Vectorization vs loop
  - [ ] 3.3 Sales matrix pipeline

- [ ] **02 — Pandas fundamentals** (`ru/` or `en/02-pandas-fundamentals-tasks.ipynb`)
  - [ ] 5.1 DataFrame basics
  - [ ] 5.2 loc / iloc
  - [ ] 5.3 Cleaning pipeline
  - [ ] 6.1–6.3 GroupBy & reshape
  - [ ] 7.1–7.3 Merge & pivot

- [ ] **03 — Pandas pipelines** (`ru/` or `en/03-pandas-pipelines-tasks.ipynb`)
  - [ ] Users + orders metrics
  - [ ] High-impact quarters
  - [ ] Cohort retention
  - [ ] Event metrics 2023
  - [ ] Regional activity
  - [ ] Cohort dashboard

- [ ] **04 — Pandas business** (`ru/` or `en/04-pandas-business-tasks.ipynb`)
  - [ ] Regional sales audit
  - [ ] Customer 360
  - [ ] Churn risk
  - [ ] Channel concentration

## Verification

```bash
# After running solution notebooks (or your own correct outputs):
pytest
```

## Mistakes log

Keep notes in [mistakes.md](mistakes.md) when something trips you up.
