from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"
full = (NOTES / "HINTS.full.md").read_text(encoding="utf-8")
idx = full.find("---\n\n<a id=")
body = full[idx:] if idx > 0 else full

ru_intro = """# Подсказки к заданиям

Напоминания, если застряли. Это **подсказки**, не готовые решения.

**Файлы:** ноутбуки с решениями, [PROGRESS.md](PROGRESS.md), [mistakes.md](mistakes.md)

English: [HINTS.en.md](HINTS.en.md)

### Навигация

**01 — NumPy:** [1.1](#задание-11) · [1.2](#задание-12) · [1.3](#задание-13) · [2.1](#задание-21) · [2.2](#задание-22) · [2.3](#задание-23) · [3.1](#задание-31) · [3.2](#задание-32) · [3.3](#задание-33) · [Босс](#boss-1)

**02 — Pandas:** [5.1](#задание-51) · [5.2](#задание-52) · [5.3](#задание-53) · [6.1](#задание-61) · [6.2](#задание-62) · [6.3](#задание-63) · [7.1](#задание-71) · [7.2](#задание-72) · [7.3](#задание-73)

**03 — Пайплайны:** [users/orders](#pipeline-1) · [Кварталы](#pipeline-2) · [Когорты](#pipeline-3) · [События](#pipeline-4) · [Регионы](#pipeline-5) · [Дашборд](#pipeline-6)

**04 — Бизнес:** [Продажи](#business-1) · [Customer 360](#business-2) · [Отток](#business-3) · [Каналы](#business-4)

**Прочее:** [Общие советы](#general-tips)

---

"""
en_intro = """# Task hints & advice

Nudges when you are stuck — not full solutions.

Russian: [HINTS.ru.md](HINTS.ru.md)

### Jump navigation

**01 — NumPy:** [1.1](#task-11) · [1.2](#task-12) · [1.3](#task-13) · [2.1](#task-21) · [2.2](#task-22) · [2.3](#task-23) · [3.1](#task-31) · [3.2](#task-32) · [3.3](#task-33) · [Boss](#boss-1)

**02 — Pandas fundamentals:** [5.1](#task-51) · [5.2](#task-52) · [5.3](#task-53) · [6.1](#task-61) · [6.2](#task-62) · [6.3](#task-63) · [7.1](#task-71) · [7.2](#task-72) · [7.3](#task-73)

**03 — Pipelines:** [Users/orders](#pipeline-1) · [Quarters](#pipeline-2) · [Cohort](#pipeline-3) · [Events](#pipeline-4) · [Regional](#pipeline-5) · [Dashboard](#pipeline-6)

**04 — Business:** [Sales](#business-1) · [Customer 360](#business-2) · [Churn](#business-3) · [Channels](#business-4)

**Other:** [General tips](#general-tips)

---

"""
body_en = body.replace("id=\"задание-", "id=\"task-").replace("### Задание", "### Task")
(NOTES / "HINTS.ru.md").write_text(ru_intro + body, encoding="utf-8")
(NOTES / "HINTS.en.md").write_text(en_intro + body_en, encoding="utf-8")
index = """# Hints index

| Language | File |
|----------|------|
| **English** | [HINTS.en.md](HINTS.en.md) |
| **Русский** | [HINTS.ru.md](HINTS.ru.md) |

Nudges only — not full solutions. Solution notebooks: [`../notebooks/`](../notebooks/).
"""
(NOTES / "HINTS.md").write_text(index, encoding="utf-8")
(NOTES / "HINTS.full.md").unlink(missing_ok=True)
print("ok")
