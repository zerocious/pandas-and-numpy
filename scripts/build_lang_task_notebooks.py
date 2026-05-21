"""Build aligned RU/EN task notebooks in notebooks/ru/ and notebooks/en/."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "notebooks"
RU = SRC / "ru"
EN = SRC / "en"

sys.path.insert(0, str(ROOT / "scripts"))
from task_notebook_content import BUSINESS, FUNDAMENTALS, NUMPY, PIPELINES  # noqa: E402

DISCLAIMER_RU = (
    "> **Disclaimer / Дисклеймер:** Тексты заданий переведены автором репозитория "
    "с помощью ИИ (Cursor AI). Это **не** профессиональный перевод. "
    "При расхождениях ориентируйтесь на код, имена файлов и "
    "[HINTS.ru.md](../../notes/HINTS.ru.md).\n"
)
DISCLAIMER_EN = (
    "> **Disclaimer:** Task descriptions were translated by the repository author "
    "using AI assistance (Cursor AI). This is **not** a professional translation. "
    "If anything is unclear, refer to code syntax, file names, and "
    "[HINTS.en.md](../../notes/HINTS.en.md).\n"
)

SETUP = [
    "from pathlib import Path\n",
    "\n",
    "ROOT = Path('../..').resolve()\n",
    "RAW = ROOT / 'data' / 'raw'\n",
    "OUT = ROOT / 'data' / 'output'\n",
    "OUT.mkdir(parents=True, exist_ok=True)\n",
]
SOL_RU = "# Ваше решение здесь\n"
SOL_EN = "# Your solution here\n"

TASKS = [
    "01-numpy-tasks.ipynb",
    "02-pandas-fundamentals-tasks.ipynb",
    "03-pandas-pipelines-tasks.ipynb",
    "04-pandas-business-tasks.ipynb",
]


def md(*lines: str) -> list[str]:
    return [line + ("\n" if not line.endswith("\n") else "") for line in lines]


def code(*lines: str) -> list[str]:
    return md(*lines)


def build_nb(
    title: str,
    disclaimer: str,
    sol: str,
    spec: list[tuple[list[str], list[str], list[str] | None]],
    lang: str,
) -> dict:
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": md(title)},
        {"cell_type": "markdown", "metadata": {}, "source": md(disclaimer)},
        {"cell_type": "code", "metadata": {}, "source": SETUP, "outputs": [], "execution_count": None},
    ]
    for ru_lines, en_lines, starter in spec:
        mlines = md(*(ru_lines if lang == "ru" else en_lines))
        cells.append({"cell_type": "markdown", "metadata": {}, "source": mlines})
        code_src: list[str] = code(*starter) if starter else []
        placeholder = SOL_EN if lang == "en" else SOL_RU
        if not code_src or not any("solution" in s.lower() or "решение" in s.lower() for s in code_src):
            code_src.append(placeholder)
        cells.append({
            "cell_type": "code",
            "metadata": {},
            "source": code_src,
            "outputs": [],
            "execution_count": None,
        })
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


BUILDERS = {
    ("01-numpy-tasks.ipynb", "ru"): lambda: build_nb(
        "# 01 — NumPy (задания)", DISCLAIMER_RU, SOL_RU, NUMPY, "ru"
    ),
    ("01-numpy-tasks.ipynb", "en"): lambda: build_nb(
        "# 01 — NumPy (tasks)", DISCLAIMER_EN, SOL_EN, NUMPY, "en"
    ),
    ("02-pandas-fundamentals-tasks.ipynb", "ru"): lambda: build_nb(
        "# 02 — Основы Pandas (задания)", DISCLAIMER_RU, SOL_RU, FUNDAMENTALS, "ru"
    ),
    ("02-pandas-fundamentals-tasks.ipynb", "en"): lambda: build_nb(
        "# 02 — Pandas fundamentals (tasks)", DISCLAIMER_EN, SOL_EN, FUNDAMENTALS, "en"
    ),
    ("03-pandas-pipelines-tasks.ipynb", "ru"): lambda: build_nb(
        "# 03 — Pandas: пайплайны (задания)", DISCLAIMER_RU, SOL_RU, PIPELINES, "ru"
    ),
    ("03-pandas-pipelines-tasks.ipynb", "en"): lambda: build_nb(
        "# 03 — Pandas data pipelines (tasks)", DISCLAIMER_EN, SOL_EN, PIPELINES, "en"
    ),
    ("04-pandas-business-tasks.ipynb", "ru"): lambda: build_nb(
        "# 04 — Pandas: бизнес-задачи (задания)", DISCLAIMER_RU, SOL_RU, BUSINESS, "ru"
    ),
    ("04-pandas-business-tasks.ipynb", "en"): lambda: build_nb(
        "# 04 — Pandas business tasks", DISCLAIMER_EN, SOL_EN, BUSINESS, "en"
    ),
}


def write_readme(folder: Path, lang: str) -> None:
    hints = "../../notes/HINTS.ru.md" if lang == "ru" else "../../notes/HINTS.en.md"
    other = "../en/README.md" if lang == "ru" else "../ru/README.md"
    other_label = "English tasks" if lang == "ru" else "Russian tasks"
    if lang == "ru":
        t = f"""# Задания (RU)

> **Disclaimer:** Тексты переведены автором репозитория с помощью ИИ (не профессиональный перевод).

| Задания | Решения |
|---------|---------|
| [01-numpy-tasks.ipynb](01-numpy-tasks.ipynb) | [../01-numpy.ipynb](../01-numpy.ipynb) |
| [02-pandas-fundamentals-tasks.ipynb](02-pandas-fundamentals-tasks.ipynb) | [../02-pandas-fundamentals.ipynb](../02-pandas-fundamentals.ipynb) |
| [03-pandas-pipelines-tasks.ipynb](03-pandas-pipelines-tasks.ipynb) | [../03-pandas-pipelines.ipynb](../03-pandas-pipelines.ipynb) |
| [04-pandas-business-tasks.ipynb](04-pandas-business-tasks.ipynb) | [../04-pandas-business.ipynb](../04-pandas-business.ipynb) |

{other_label}: [{other}]({other}) · Подсказки: [{hints}]({hints})
"""
    else:
        t = f"""# Tasks (EN)

> **Disclaimer:** Wording translated by the repository author using AI (not a professional translation).

| Tasks | Solutions |
|-------|-----------|
| [01-numpy-tasks.ipynb](01-numpy-tasks.ipynb) | [../01-numpy.ipynb](../01-numpy.ipynb) |
| [02-pandas-fundamentals-tasks.ipynb](02-pandas-fundamentals-tasks.ipynb) | [../02-pandas-fundamentals.ipynb](../02-pandas-fundamentals.ipynb) |
| [03-pandas-pipelines-tasks.ipynb](03-pandas-pipelines-tasks.ipynb) | [../03-pandas-pipelines.ipynb](../03-pandas-pipelines.ipynb) |
| [04-pandas-business-tasks.ipynb](04-pandas-business-tasks.ipynb) | [../04-pandas-business.ipynb](../04-pandas-business.ipynb) |

{other_label}: [{other}]({other}) · Hints: [{hints}]({hints})
"""
    (folder / "README.md").write_text(t, encoding="utf-8")


def main() -> None:
    RU.mkdir(parents=True, exist_ok=True)
    EN.mkdir(parents=True, exist_ok=True)
    for name in TASKS:
        for lang, dest in (("ru", RU), ("en", EN)):
            nb = BUILDERS[(name, lang)]()
            path = dest / name
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
            print("wrote", lang, name)
    write_readme(RU, "ru")
    write_readme(EN, "en")
    print("done")


if __name__ == "__main__":
    main()
