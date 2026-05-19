"""Strip execution outputs from notebooks before commit."""
import json
from pathlib import Path

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"


def main() -> None:
    for path in NB_DIR.glob("*.ipynb"):
        nb = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "code":
                if cell.get("outputs") or cell.get("execution_count") is not None:
                    cell["outputs"] = []
                    cell["execution_count"] = None
                    changed = True
        if changed:
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
            print("cleared", path.name)


if __name__ == "__main__":
    main()
