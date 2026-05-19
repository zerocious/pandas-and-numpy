"""Build RU and EN task notebooks in notebooks/ru/ and notebooks/en/."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "notebooks"
RU = SRC / "ru"
EN = SRC / "en"

DISCLAIMER_RU = (
    "> **Disclaimer / Дисклеймер:** Тексты заданий переведены автором репозитория "
    "с помощью ИИ (Cursor AI). Это **не** профессиональный перевод. "
    "При расхождениях ориентируйтесь на код, имена файлов и [HINTS.md](../../notes/HINTS.md).\n"
)
DISCLAIMER_EN = (
    "> **Disclaimer:** Task descriptions were translated by the repository author "
    "using AI assistance (Cursor AI). This is **not** a professional translation. "
    "If anything is unclear, refer to code syntax, file names, and [HINTS.md](../../notes/HINTS.md).\n"
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


def build_nb(title: str, disclaimer: str, sol: str, pairs: list[tuple[list[str], list[str]]]) -> dict:
    """pairs: list of (markdown_lines, code_lines) per exercise."""
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": md(title)},
        {"cell_type": "markdown", "metadata": {}, "source": md(disclaimer)},
        {"cell_type": "code", "metadata": {}, "source": SETUP, "outputs": [], "execution_count": None},
    ]
    for mlines, clines in pairs:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": mlines})
        src = clines if clines else [sol]
        if not any("solution" in s.lower() or "решение" in s.lower() for s in src):
            src = src + [sol]
        cells.append({
            "cell_type": "code",
            "metadata": {},
            "source": src,
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


# --- 01 NumPy ---
def numpy_ru():
    return build_nb(
        "# 01 — NumPy (задания)",
        DISCLAIMER_RU,
        SOL_RU,
        [
            (md(
                "## Задание 1.1",
                "Создайте массив из списка [10, 20, 30, 40, 50, 60].",
                "Выведите его shape, ndim, size, dtype.",
                "Создайте матрицу 3×4, заполненную единицами, и матрицу 2×5, заполненную числом 7.5.",
                "Сгенерируйте массив из 8 чисел от 0 до 14 с шагом 2.",
            ), []),
            (md(
                "## Задание 1.2",
                "Создайте массив чисел от 0 до 23 (np.arange).",
                "Преобразуйте его в матрицу 4×6.",
                "Преобразуйте ту же последовательность в 3D-тензор формы (2, 3, 4), используя -1 для одной из осей.",
                "Возьмите матрицу 4×6, сделайте её одномерной через ravel(), измените первый элемент на 999 и проверьте, изменился ли исходник.",
                "Повторите шаг 4 через flatten(). Что произошло?",
            ), []),
            (md(
                "## Задание 1.3",
                "Сгенерируйте массив из 10 000 случайных чисел от 50 до 1500 (np.random.uniform).",
                "Проверьте dtype и размер в байтах (arr.nbytes).",
                "Приведите массив к float32, снова проверьте nbytes. Насколько сократилась память?",
                "Округлите все значения до 2 знаков (векторно, без цикла).",
                "Преобразуйте массив в форму (250, 40) — таблица «250 дней × 40 категорий».",
            ), []),
            (md(
                "## Задание 2.1",
                "Создайте 1D-массив из 30 элементов (числа 1…30).",
                "Срез: элементы с 10-го по 20-й включительно.",
                "Булева маска для чётных чисел.",
                "Замените все значения < 15 на -1 в исходном массиве. Выведите первые 10 элементов.",
            ), []),
            (md(
                "## Задание 2.2",
                "Матрица 5×5 случайных целых от 10 до 90.",
                "Числа < 30 → 0, > 70 → 100 (np.where или np.select).",
                "Индексы элементов, равных 100 (np.argwhere / np.where).",
                "Обнулите последний столбец срезом.",
            ), []),
            (md(
                "## Задание 2.3",
                "Матрица 1000×3: суммы ~N(500,200), кол-во товаров [1,10], возврат [0,1].",
                "Фильтр: сумма > 800 и возврат == 0. Доля таких строк.",
                "Столбец segment: Premium / Standard / Low (по условиям из задания).",
                "Добавьте segment как 4-й столбец (dtype=object).",
            ), []),
            (md(
                "## Задание 3.1",
                "Матрица 4×5 случайных чисел.",
                "Прибавьте к каждой строке [1,2,3,4,5].",
                "Прибавьте [10,20,30,40] по столбцам (исправьте ValueError через newaxis/reshape).",
                "Умножьте каждый элемент на максимум матрицы.",
            ), []),
            (md(
                "## Задание 3.2",
                "1 000 000 чисел N(0,1).",
                "Функция с for: x>0 → x², иначе abs(x). Замер времени.",
                "Векторный вариант через np.where. Замер времени.",
                "Выведите time_loop / time_vec.",
            ), []),
            (md(
                "## Задание 3.3",
                "Матрица (1000, 5) случайных положительных чисел.",
                "Min и max по каждому столбцу (axis=0).",
                "Min–max нормализация: (x - min) / (max - min) одной строкой.",
                "Проверьте: min столбца ≈ 0, max ≈ 1.",
            ), []),
            (md(
                "## Босс-файт: векторная подготовка датасета",
                "1. Клиппинг: значения > 95-го перцентиля → p95 (NaN не трогать).",
                "2. Импутация: NaN → медиана столбца.",
                "3. Сегменты VIP / Active / AtRisk / Standard (np.select, приоритет сверху вниз).",
                "4. Min–max нормализация 4 числовых столбцов.",
                "**Ограничения:** только NumPy, без циклов for/while, < 0.3 сек.",
            ), []),
        ],
    )


def numpy_en():
    return build_nb(
        "# 01 — NumPy (tasks)",
        DISCLAIMER_EN,
        SOL_EN,
        [
            (md(
                "## Task 1.1",
                "Create an array from [10, 20, 30, 40, 50, 60].",
                "Print its shape, ndim, size, and dtype.",
                "Create a 3×4 matrix of ones and a 2×5 matrix filled with 7.5.",
                "Generate 8 numbers from 0 to 14 with step 2.",
            ), []),
            (md(
                "## Task 1.2",
                "Create an array 0…23 with np.arange.",
                "Reshape to 4×6.",
                "Reshape the same data to a 3D tensor (2, 3, 4) using -1 for one axis.",
                "Ravel the 4×6 matrix, set first element to 999 — did the original change?",
                "Repeat with flatten(). What happened?",
            ), []),
            (md(
                "## Task 1.3",
                "10,000 random floats from 50 to 1500 (np.random.uniform).",
                "Check dtype and nbytes.",
                "Cast to float32; check nbytes again. How much memory saved?",
                "Round to 2 decimals (vectorized, no loop).",
                "Reshape to (250, 40).",
            ), []),
            (md(
                "## Task 2.1",
                "1D array 1…30.",
                "Slice elements 10 through 20 inclusive.",
                "Boolean mask for even numbers.",
                "Replace values < 15 with -1 in place; print first 10 elements.",
            ), []),
            (md(
                "## Task 2.2",
                "5×5 random integers from 10 to 90.",
                "Values < 30 → 0, > 70 → 100 (np.where / np.select).",
                "Indices where value equals 100.",
                "Zero the last column with slicing.",
            ), []),
            (md(
                "## Task 2.3",
                "1000×3 matrix: amounts ~N(500,200), item count [1,10], return flag [0,1].",
                "Filter amount > 800 and return == 0; compute their share.",
                "Add segment column Premium / Standard / Low.",
                "Append as 4th column (object dtype).",
            ), []),
            (md(
                "## Task 3.1",
                "4×5 random matrix.",
                "Add [1,2,3,4,5] to each row.",
                "Add [10,20,30,40] per column (fix shape with newaxis).",
                "Multiply every element by the matrix maximum.",
            ), []),
            (md(
                "## Task 3.2",
                "1,000,000 draws from N(0,1).",
                "for-loop: square if positive else abs; time it.",
                "Vectorized np.where version; time it.",
                "Print time_loop / time_vec.",
            ), []),
            (md(
                "## Task 3.3",
                "(1000, 5) positive random matrix.",
                "Min/max per column.",
                "Min–max scale to [0, 1] in one expression.",
                "Verify column mins ≈ 0 and maxes ≈ 1.",
            ), []),
            (md(
                "## Boss fight: vector data prep",
                "1. Clip values above the 95th percentile per column.",
                "2. Fill NaN with column median.",
                "3. Segments VIP / Active / AtRisk / Standard via np.select.",
                "4. Min–max normalize four numeric columns.",
                "**Rules:** NumPy only, no for/while loops, runtime < 0.3s.",
            ), []),
        ],
    )


# Import extended builders from companion module pattern - define 02,03,04 inline below

def pandas_fundamentals_ru():
    return build_nb("# 02 — Основы Pandas (задания)", DISCLAIMER_RU, SOL_RU, [
        (md("## Задание 5.1", "DataFrame из словаря (user_id, status, revenue).", "df.info(); user_id → str, status → category.", "Фильтр: status=='active' и revenue>200.", "Колонки user_id и revenue."), []),
        (md("## Задание 5.2", "DataFrame 5×3, индекс A–E, колонки x,y,z, числа 1–15.", ".loc: C,y=999; .iloc: последняя строка=0.", "Подтаблица x,z для B,D; z=-1 через .copy()."), []),
        (md("## Задание 5.3", "Сгенерируйте orders: ORD-0001…, date_str DD.MM.YYYY, amount с NaN и минусами, region.", "Даты → datetime; только 2024 год.", "NaN→0; amount>=0; tier High/Low (np.where).", "Сохранить clean_orders.csv (index=False)."), []),
        (md("## Задание 6.1", "category, product, sales.", "Сумма по category.", "Сумма и среднее по category+product (именованные agg)."), []),
        (md("## Задание 6.2", "user_id, region, order_amount, is_completed.", "groupby region: total_revenue, avg_order, completed_orders, total_orders.", "Фильтр total_orders>=50; reset_index."), []),
        (md("## Задание 6.3", "user_id, category, monthly_spend.", "transform: category_avg_spend.", "spend_share; is_high_value (>1.5× среднего)."), []),
        (md("## Задание 7.1", "df_users + df_orders; left merge validate 1:m.", "fillna amount; выручка по tier."), []),
        (md("## Задание 7.2", "q1,q2,q3 → concat; quarter Q1–Q3.", "pivot_table; growth_q3_vs_q2."), []),
        (md("## Задание 7.3", "melt city + месяцы; доля месяца от города; фильтр share>0.35."), []),
    ])


def pandas_fundamentals_en():
    return build_nb("# 02 — Pandas fundamentals (tasks)", DISCLAIMER_EN, SOL_EN, [
        (md("## Task 5.1", "DataFrame from dict (user_id, status, revenue).", "df.info(); cast user_id to str, status to category.", "Filter active and revenue>200.", "Columns user_id, revenue only."), []),
        (md("## Task 5.2", "5×3 DataFrame, index A–E, columns x,y,z, values 1–15.", ".loc C,y=999; .iloc last row=0.", "Subset x,z for rows B,D; set z=-1 using .copy()."), []),
        (md("## Task 5.3", "Synthetic orders: ORD ids, DD.MM.YYYY dates, amounts with NaN/negatives, regions.", "Parse dates; keep 2024 only.", "fillna 0; drop negatives; tier with np.where.", "Save clean_orders.csv."), []),
        (md("## Task 6.1", "category, product, sales.", "Sum per category.", "Sum and mean per category+product (named agg)."), []),
        (md("## Task 6.2", "Group by region: revenue, avg, completed count, order count.", "Filter total_orders>=50; reset_index."), []),
        (md("## Task 6.3", "transform mean per category; spend_share; is_high_value flag."), []),
        (md("## Task 7.1", "left merge users/orders validate 1:m; fillna; revenue by tier."), []),
        (md("## Task 7.2", "concat quarters; pivot_table; Q3 minus Q2 growth."), []),
        (md("## Task 7.3", "melt wide months; city revenue share; filter share>0.35."), []),
    ])


def pipelines_ru():
    return build_nb("# 03 — Pandas: пайплайны (задания)", DISCLAIMER_RU, SOL_RU, [
        (md(
            "## Пайплайн: users + orders → metrics_by_region",
            "users.csv + orders.csv; dtype; user_id str.",
            "left merge validate 1:m; заказы 2023 года; fillna amount.",
            "По region: total_revenue, avg_order, active_users; revenue_share.",
            "→ metrics_by_region.csv",
        ), code("# U0001,01.01.2022,EU")),
        (md(
            "## Высокодоходные кварталы (sales_wide)",
            "melt; total_year transform sum;",
            "фильтр revenue > 0.35 * total_year;",
            "pivot_table → high_impact_quarters.csv",
        ), code("# Widget_A,North,9980,...")),
        (md(
            "## Когортное удержание (transactions)",
            "Очистка amount>0; cohort и tx_month YYYY-MM;",
            "active_users; cohort_size; retention_rate;",
            "фильтр cohort_size>=20, месяцы 0–5;",
            "→ cohort_retention_real.csv",
        ), code("1. Загрузите transactions.csv")),
        (md(
            "## Метрики событий (raw_events)",
            "dtype; даты DD.MM.YYYY; dedupe event_id;",
            "медиана value по event_type; 2023 год;",
            "share_of_total; → event_metrics_2023.csv utf-8-sig",
        ), []),
        (md(
            "## Региональная активность (users + sessions)",
            "даты; merge; user_tenure_days;",
            "agg по region; active_users>=30;",
            "→ regional_activity.csv",
        ), []),
        (md(
            "## Когортный дашборд",
            "dedupe; cohort; month_diff 0–5;",
            "revenue_retention pivot;",
            "→ cohort_dashboard.csv",
        ), []),
    ])


def pipelines_en():
    return build_nb("# 03 — Pandas data pipelines (tasks)", DISCLAIMER_EN, SOL_EN, [
        (md(
            "## Pipeline: users + orders → metrics_by_region",
            "Load users.csv and orders.csv; cast user_id to str.",
            "left merge validate 1:m; filter orders year 2023; fillna amount.",
            "Per region: total_revenue, avg_order, active_users; revenue_share.",
            "Save metrics_by_region.csv",
        ), code("# U0001,01.01.2022,EU")),
        (md(
            "## High-impact quarters (sales_wide)",
            "melt; total_year with transform sum;",
            "filter revenue > 35% of annual pair total;",
            "pivot → high_impact_quarters.csv",
        ), code("# sample row")),
        (md(
            "## Cohort retention (transactions)",
            "Drop amount<=0; cohort & tx_month;",
            "retention_rate; filter cohort_size>=20, months 0–5;",
            "Save cohort_retention_real.csv",
        ), code("1. Load transactions.csv")),
        (md(
            "## Event metrics (raw_events)",
            "Parse dates; dedupe; median impute;",
            "2023 only; share_of_total;",
            "Save event_metrics_2023.csv",
        ), []),
        (md(
            "## Regional activity (users + sessions)",
            "Parse dates; merge; tenure days;",
            "Aggregate by region; filter active_users>=30;",
            "Save regional_activity.csv",
        ), []),
        (md(
            "## Cohort dashboard",
            "Dedupe; cohort months; month_diff 0–5;",
            "Pivot revenue_retention;",
            "Save cohort_dashboard.csv",
        ), []),
    ])


def business_ru():
    return build_nb("# 04 — Pandas: бизнес-задачи (задания)", DISCLAIMER_RU, SOL_RU, [
        (md(
            "## Задача: аудит региональных продаж",
            "Широкий формат по месяцам → long (product, region, month).",
            "Доля месяца в годовой выручке пары product–region.",
            "Фильтр доли > 22%; сводная product × region.",
            "Экспорт CSV. Разрешено: melt, transform, pivot_table.",
        ), []),
        (md(
            "## Задача 1: Customer 360",
            "crm_raw + billing_raw; dedupe; left merge.",
            "Медиана signup_date по региону; is_high_value (>200).",
            "→ customer_master.csv",
        ), []),
        (md(
            "## Задача 2: риск оттока (user_events)",
            "Сессии: разрыв > 30 мин (diff + cumsum).",
            "monthly_avg_duration vs 70% личного baseline.",
            "≥3 активных месяца; → churn_risk_analysis.csv",
        ), []),
        (md(
            "## Задача 3: концентрация каналов",
            "melt channel_sales_wide; три доли; HHI;",
            "risk_class; product summary + idxmax;",
            "→ channel_pairs_long.csv, product_concentration_summary.csv",
        ), code(
            "# После чтения файла: годовая выручка по каналам.",
            "# melt широкой таблицы в длинную.",
        )),
    ])


def business_en():
    src = json.loads((SRC / "04-pandas-business-tasks.ipynb").read_text(encoding="utf-8"))
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": md("# 04 — Pandas business tasks")},
        {"cell_type": "markdown", "metadata": {}, "source": md(DISCLAIMER_EN)},
        {"cell_type": "code", "metadata": {}, "source": SETUP, "outputs": [], "execution_count": None},
    ]
    for cell in src["cells"][2:]:
        if cell["cell_type"] == "markdown":
            cells.append({"cell_type": "markdown", "metadata": {}, "source": cell["source"]})
        elif cell["cell_type"] == "code":
            src_lines = cell.get("source", [])
            if "ROOT = Path" in "".join(src_lines):
                continue
            new = []
            for line in src_lines:
                if "Your solution" in line:
                    new.append(SOL_EN)
                else:
                    new.append(line)
            if not new:
                new = [SOL_EN]
            cells.append({"cell_type": "code", "metadata": {}, "source": new, "outputs": [], "execution_count": None})
    return {
        "cells": cells,
        "metadata": src.get("metadata", {}),
        "nbformat": 4,
        "nbformat_minor": 5,
    }


BUILDERS = {
    ("01-numpy-tasks.ipynb", "ru"): numpy_ru,
    ("01-numpy-tasks.ipynb", "en"): numpy_en,
    ("02-pandas-fundamentals-tasks.ipynb", "ru"): pandas_fundamentals_ru,
    ("02-pandas-fundamentals-tasks.ipynb", "en"): pandas_fundamentals_en,
    ("03-pandas-pipelines-tasks.ipynb", "ru"): pipelines_ru,
    ("03-pandas-pipelines-tasks.ipynb", "en"): pipelines_en,
    ("04-pandas-business-tasks.ipynb", "ru"): business_ru,
    ("04-pandas-business-tasks.ipynb", "en"): business_en,
}


def write_readme(folder: Path, lang: str) -> None:
    if lang == "ru":
        t = """# Задания (RU)

> **Disclaimer:** Тексты переведены автором репозитория с помощью ИИ (не профессиональный перевод).

| Задания | Решения |
|---------|---------|
| [01-numpy-tasks.ipynb](01-numpy-tasks.ipynb) | [../01-numpy.ipynb](../01-numpy.ipynb) |
| [02-pandas-fundamentals-tasks.ipynb](02-pandas-fundamentals-tasks.ipynb) | [../02-pandas-fundamentals.ipynb](../02-pandas-fundamentals.ipynb) |
| [03-pandas-pipelines-tasks.ipynb](03-pandas-pipelines-tasks.ipynb) | [../03-pandas-pipelines.ipynb](../03-pandas-pipelines.ipynb) |
| [04-pandas-business-tasks.ipynb](04-pandas-business-tasks.ipynb) | [../04-pandas-business.ipynb](../04-pandas-business.ipynb) |

English tasks: [../en/README.md](../en/README.md) · Hints: [../../notes/HINTS.md](../../notes/HINTS.md)
"""
    else:
        t = """# Tasks (EN)

> **Disclaimer:** Wording translated by the repository author using AI (not a professional translation).

| Tasks | Solutions |
|-------|-----------|
| [01-numpy-tasks.ipynb](01-numpy-tasks.ipynb) | [../01-numpy.ipynb](../01-numpy.ipynb) |
| [02-pandas-fundamentals-tasks.ipynb](02-pandas-fundamentals-tasks.ipynb) | [../02-pandas-fundamentals.ipynb](../02-pandas-fundamentals.ipynb) |
| [03-pandas-pipelines-tasks.ipynb](03-pandas-pipelines-tasks.ipynb) | [../03-pandas-pipelines.ipynb](../03-pandas-pipelines.ipynb) |
| [04-pandas-business-tasks.ipynb](04-pandas-business-tasks.ipynb) | [../04-pandas-business.ipynb](../04-pandas-business.ipynb) |

Russian tasks: [../ru/README.md](../ru/README.md) · Hints: [../../notes/HINTS.md](../../notes/HINTS.md)
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
