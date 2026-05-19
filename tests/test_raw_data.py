from pathlib import Path

import pandas as pd
import pytest

RAW_FILES = [
    "users.csv",
    "orders.csv",
    "transactions.csv",
    "sales_wide.csv",
    "raw_events.csv",
    "sessions.csv",
    "regional_sales_wide.csv",
    "crm_raw.csv",
    "billing_raw.csv",
    "user_events.csv",
    "channel_sales_wide.csv",
]


@pytest.mark.parametrize("filename", RAW_FILES)
def test_raw_files_exist(raw_dir: Path, filename: str) -> None:
    path = raw_dir / filename
    assert path.exists(), f"Missing raw file: {filename}"
    assert path.stat().st_size > 0


def test_users_schema(raw_dir: Path) -> None:
    df = pd.read_csv(raw_dir / "users.csv", nrows=5)
    assert {"user_id", "region", "signup_date"}.issubset(df.columns)
