"""Validate notebook exports in data/output/ (run solution notebooks first)."""

from pathlib import Path

import pandas as pd
import pytest

from conftest import require_output


@pytest.fixture
def metrics_by_region(out_dir: Path) -> pd.DataFrame:
    path = require_output(out_dir / "metrics_by_region.csv")
    return pd.read_csv(path)


def test_metrics_by_region_columns(metrics_by_region: pd.DataFrame) -> None:
    expected = {"total_revenue", "avg_order", "active_users", "revenue_share"}
    assert expected.issubset(metrics_by_region.columns)


def test_metrics_revenue_share_sums_to_one(metrics_by_region: pd.DataFrame) -> None:
    assert metrics_by_region["revenue_share"].sum() == pytest.approx(1.0, rel=1e-5)


def test_clean_orders_2024_only(out_dir: Path) -> None:
    path = require_output(out_dir / "clean_orders.csv")
    df = pd.read_csv(path, parse_dates=["date"])
    assert (df["date"].dt.year == 2024).all()
    assert (df["amount"] >= 0).all()
    assert df["tier"].isin(["High", "Low"]).all()


def test_cohort_retention_bounds(out_dir: Path) -> None:
    path = require_output(out_dir / "cohort_retention_real.csv")
    df = pd.read_csv(path)
    assert "retention_rate" in df.columns
    assert df["retention_rate"].between(0, 1).all()


def test_event_metrics_share(out_dir: Path) -> None:
    path = require_output(out_dir / "event_metrics_2023.csv")
    df = pd.read_csv(path)
    assert "share_of_total" in df.columns
    assert df["share_of_total"].sum() == pytest.approx(1.0, rel=1e-5)


def test_churn_risk_columns(out_dir: Path) -> None:
    path = require_output(out_dir / "churn_risk_analysis.csv")
    df = pd.read_csv(path)
    for col in ("user_id", "is_at_risk", "monthly_avg_duration"):
        assert col in df.columns


def test_channel_pairs_long(out_dir: Path) -> None:
    path = require_output(out_dir / "channel_pairs_long.csv")
    df = pd.read_csv(path)
    assert {"product", "channel", "revenue", "risk_class"}.issubset(df.columns)
