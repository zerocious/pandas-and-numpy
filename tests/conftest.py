from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "output"


@pytest.fixture(scope="session")
def project_root() -> Path:
    return ROOT


@pytest.fixture(scope="session")
def raw_dir() -> Path:
    return RAW


@pytest.fixture(scope="session")
def out_dir() -> Path:
    return OUT


def require_output(path: Path) -> Path:
    if not path.exists() or path.stat().st_size == 0:
        pytest.skip(f"Missing output — run solution notebooks first: {path.name}")
    return path
