"""Convert ## comment blocks in task notebooks into markdown cells."""
from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"
SOLUTION_MARKER = "# Your solution here"


def comment_to_md(line: str) -> str:
    s = line.rstrip("\n")
    if s.lstrip().startswith("#"):
        s = re.sub(r"^\s*#{1,2}\s?", "", s)
        return s + "\n"
    return s


def split_code_cell(cell: dict) -> list[dict]:
    lines = cell.get("source", [])
    comment_lines: list[str] = []
    code_lines: list[str] = []

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#") and SOLUTION_MARKER not in line:
            comment_lines.append(line)
        elif stripped.startswith(SOLUTION_MARKER) or stripped == "# Your solution here\n":
            code_lines.append("# Your solution here\n")
        elif stripped in ("", "\n") and not code_lines:
            comment_lines.append(line)
        else:
            code_lines.append(line)

    if not comment_lines:
        return [cell]

    md_source = [comment_to_md(l) for l in comment_lines]
    while md_source and md_source[-1].strip() == "":
        md_source.pop()

    out: list[dict] = []
    if any(s.strip() for s in md_source):
        out.append({"cell_type": "markdown", "metadata": {}, "source": md_source})

    code_source = code_lines if code_lines else ["# Your solution here\n"]
    out.append(
        {
            "cell_type": "code",
            "metadata": cell.get("metadata", {}),
            "source": code_source,
            "outputs": [],
            "execution_count": None,
        }
    )
    return out


def convert_notebook(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    new_cells: list[dict] = []

    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            new_cells.append(cell)
            continue
        if cell["cell_type"] != "code":
            new_cells.append(cell)
            continue

        src = "".join(cell.get("source", []))
        is_setup = "ROOT = Path" in src and "RAW =" in src
        has_task_comments = any(
            l.lstrip().startswith("##") or l.lstrip().startswith("# Задание")
            for l in cell.get("source", [])
        )

        if is_setup or not has_task_comments:
            c = deepcopy(cell)
            c["outputs"] = []
            c["execution_count"] = None
            new_cells.append(c)
        else:
            new_cells.extend(split_code_cell(cell))

    nb["cells"] = new_cells
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"converted {path.name} -> {len(new_cells)} cells")


def main() -> None:
    for path in sorted(NB_DIR.glob("*-tasks.ipynb")):
        convert_notebook(path)


if __name__ == "__main__":
    main()
