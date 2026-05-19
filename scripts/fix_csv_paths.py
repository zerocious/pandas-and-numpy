import json
import re
from pathlib import Path

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"
PAT = re.compile(r"""\.to_csv\(\s*['"]([^'"]+)['"]""")


def main() -> None:
    for path in NB_DIR.glob("*.ipynb"):
        if path.name.endswith("-tasks.ipynb") or path.name == "00-index.ipynb":
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for cell in nb["cells"]:
            if cell.get("cell_type") != "code":
                continue
            new_src = []
            for line in cell.get("source", []):
                new_line = PAT.sub(lambda m: f".to_csv(str(OUT / '{m.group(1)}')", line)
                changed = changed or new_line != line
                new_src.append(new_line)
            cell["source"] = new_src
        if changed:
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
            print("fixed", path.name)


if __name__ == "__main__":
    main()
