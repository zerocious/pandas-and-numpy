"""Split monolithic notebooks into topic-based parts."""
from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"

SETUP_CELL = {
    "cell_type": "code",
    "metadata": {},
    "source": [
        "from pathlib import Path\n",
        "\n",
        "ROOT = Path('..').resolve()\n",
        "RAW = ROOT / 'data' / 'raw'\n",
        "OUT = ROOT / 'data' / 'output'\n",
        "OUT.mkdir(parents=True, exist_ok=True)\n",
    ],
    "outputs": [],
    "execution_count": None,
}

SPLITS = [
    {
        "slug": "01-numpy",
        "title": "01 — NumPy",
        "start": 0,
        "until": lambda t: "## Задание 5.1" in t or "## Задание 5.1" in t,
    },
    {
        "slug": "02-pandas-fundamentals",
        "title": "02 — Pandas fundamentals",
        "start": lambda cells, i: i,
        "until": lambda t: "🔴 Задача «Сквозной пайплайн" in t,
    },
    {
        "slug": "03-pandas-pipelines",
        "title": "03 — Pandas data pipelines",
        "until": lambda t: "Regional Sales Audit" in t or "## 📊 TASK: Regional Sales" in t,
    },
    {
        "slug": "04-pandas-business",
        "title": "04 — Pandas business tasks",
        "until": lambda t: False,
    },
]


def cell_text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def clear_cell(cell: dict) -> dict:
    c = deepcopy(cell)
    if c["cell_type"] == "code":
        c["outputs"] = []
        c["execution_count"] = None
    for key in ("id",):
        c.pop(key, None)
    return c


def classify(cells: list[dict]) -> list[tuple[str, list[dict]]]:
    buckets: list[list[dict]] = [[], [], [], []]
    idx = 0
    for cell in cells:
        text = cell_text(cell)
        if idx == 0 and "## Задание 5.1" in text:
            idx = 1
        elif idx == 1 and "🔴 Задача «Сквозной пайплайн" in text:
            idx = 2
        elif idx == 2 and ("Regional Sales Audit" in text or "## 📊 TASK: Regional Sales" in text):
            idx = 3
        buckets[idx].append(cell)
    slugs = ["01-numpy", "02-pandas-fundamentals", "03-pandas-pipelines", "04-pandas-business"]
    return list(zip(slugs, buckets))


def update_paths(source: list[str]) -> list[str]:
    """Normalize CSV paths to RAW/OUT helpers where possible."""
    out = []
    for line in source:
        s = line
        s = re.sub(r"['\"]\.\./data/raw/([^'\"]+)['\"]", r"str(RAW / '\1')", s)
        s = re.sub(r"['\"]\.\./data/output/([^'\"]+)['\"]", r"str(OUT / '\1')", s)
        out.append(s)
    return out


def build_notebook(title: str, cells: list[dict], tasks_only: bool = False) -> dict:
    body = []
    intro = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"# {title}\n"],
    }
    body.append(intro)
    body.append(deepcopy(SETUP_CELL))

    for cell in cells:
        c = clear_cell(cell)
        if tasks_only and c["cell_type"] == "code":
            c = tasks_cell(c)
        elif c["cell_type"] == "code":
            c["source"] = update_paths(c.get("source", []))
        body.append(c)

    return {
        "cells": body,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def tasks_cell(cell: dict) -> dict:
    lines = cell.get("source", [])
    kept = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#") or stripped in ("", "\n"):
            kept.append(line)
        elif not kept:
            continue
        else:
            break
    while kept and kept[-1].strip() == "":
        kept.pop()
    if not any(l.lstrip().startswith("#") for l in kept):
        kept = []
    if kept and not kept[-1].endswith("\n"):
        kept[-1] += "\n"
    kept.append("\n# Your solution here\n")
    cell["source"] = kept
    return cell


def write_nb(path: Path, nb: dict) -> None:
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> None:
    src_path = NOTEBOOKS / "NumPy.ipynb"
    nb = json.loads(src_path.read_text(encoding="utf-8"))
    classified = classify(nb["cells"])

    titles = {
        "01-numpy": "01 — NumPy",
        "02-pandas-fundamentals": "02 — Pandas fundamentals",
        "03-pandas-pipelines": "03 — Pandas data pipelines",
        "04-pandas-business": "04 — Pandas business tasks",
    }

    for slug, cells in classified:
        if not cells:
            raise SystemExit(f"No cells for {slug}")
        sol = build_notebook(titles[slug], cells, tasks_only=False)
        tasks = build_notebook(titles[slug] + " (tasks)", cells, tasks_only=True)
        write_nb(NOTEBOOKS / f"{slug}.ipynb", sol)
        write_nb(NOTEBOOKS / f"{slug}-tasks.ipynb", tasks)
        print(f"{slug}: {len(cells)} cells")

    # Index notebook
    index = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Pandas & NumPy — course notebooks\n",
                    "\n",
                    "| Notebook | Tasks-only |\n",
                    "|----------|------------|\n",
                    "| [01-numpy.ipynb](01-numpy.ipynb) | [01-numpy-tasks.ipynb](01-numpy-tasks.ipynb) |\n",
                    "| [02-pandas-fundamentals.ipynb](02-pandas-fundamentals.ipynb) | [02-pandas-fundamentals-tasks.ipynb](02-pandas-fundamentals-tasks.ipynb) |\n",
                    "| [03-pandas-pipelines.ipynb](03-pandas-pipelines.ipynb) | [03-pandas-pipelines-tasks.ipynb](03-pandas-pipelines-tasks.ipynb) |\n",
                    "| [04-pandas-business.ipynb](04-pandas-business.ipynb) | [04-pandas-business-tasks.ipynb](04-pandas-business-tasks.ipynb) |\n",
                    "\n",
                    "**How to study:** work through the `*-tasks.ipynb` notebooks first, then compare with the solution notebooks.\n",
                ],
            }
        ],
        "metadata": {"language_info": {"name": "python"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    write_nb(NOTEBOOKS / "00-index.ipynb", index)

    # Remove monolithic notebooks
    for old in ("NumPy.ipynb", "NumPy - Solutions.ipynb", "NumPy - Tasks.ipynb"):
        p = NOTEBOOKS / old
        if p.exists():
            p.unlink()
            print(f"removed {old}")


if __name__ == "__main__":
    main()
