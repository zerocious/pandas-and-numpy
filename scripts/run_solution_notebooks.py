"""Execute all solution notebooks to regenerate data/output/."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("[0-9][0-9]-*.ipynb"))
NOTEBOOKS = [p for p in NOTEBOOKS if not p.name.endswith("-tasks.ipynb") and p.name != "00-index.ipynb"]


def main() -> int:
    for nb in NOTEBOOKS:
        print(f"Executing {nb.name} ...")
        rc = subprocess.call(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                str(nb),
                "--ExecutePreprocessor.timeout=300",
            ],
            cwd=ROOT / "notebooks",
        )
        if rc != 0:
            print(f"Failed: {nb.name}")
            return rc
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
