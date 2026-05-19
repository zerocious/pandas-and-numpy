"""Apply code-quality fixes to solution notebooks."""
from __future__ import annotations

import json
import re
from pathlib import Path

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"


def fix_line(line: str) -> str:
    s = line
    s = re.sub(r"\.transform\(sum\)", '.transform("sum")', s)
    s = re.sub(r"\.transform\(sum\)\.copy\(\)", '.transform("sum")', s)
    # Redundant copy after agg/groupby into new variable
    s = re.sub(
        r"(\.groupby\([^)]+\)\.(?:agg|apply|transform)\([^)]*\)(?:\.\w+\([^)]*\))*)\.copy\(\)",
        r"\1",
        s,
    )
    s = re.sub(r"(pd\.pivot_table\([^;]+\))\.copy\(\)", r"\1", s)
    s = re.sub(r"(\.reset_index\(\))\.copy\(\)", r"\1", s)
    s = re.sub(r"(\.melt\([^;]+\))\.copy\(\)", r"\1", s)
    # export without index (task standard)
    s = s.replace("index=True, encoding='utf-8-sig'", "index=False, encoding='utf-8-sig'")
    return s


def main() -> None:
    for path in sorted(NB_DIR.glob("*.ipynb")):
        if path.name.endswith("-tasks.ipynb") or path.name == "00-index.ipynb":
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for cell in nb["cells"]:
            if cell.get("cell_type") != "code":
                continue
            cell["outputs"] = []
            cell["execution_count"] = None
            new_src = []
            for line in cell.get("source", []):
                nl = fix_line(line)
                changed = changed or nl != line
                new_src.append(nl)
            cell["source"] = new_src
        nb_path = path
        nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
        print("updated", path.name)


if __name__ == "__main__":
    main()
