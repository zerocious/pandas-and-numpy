"""Write one sample row per output CSV to docs/samples/."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "output"
SAMPLES = ROOT / "docs" / "samples"
SAMPLES.mkdir(parents=True, exist_ok=True)

FILES = [
    "metrics_by_region.csv",
    "high_impact_quarters.csv",
    "cohort_retention_real.csv",
    "event_metrics_2023.csv",
    "regional_activity.csv",
    "cohort_dashboard.csv",
    "clean_orders.csv",
    "customer_master.csv",
    "churn_risk_analysis.csv",
    "channel_pairs_long.csv",
    "product_concentration_summary.csv",
    "Regional_Sales_Audit_Summary.csv",
]


def main() -> None:
    for name in FILES:
        path = OUT / name
        if not path.exists() or path.stat().st_size == 0:
            print("skip (missing):", name)
            continue
        df = pd.read_csv(path, nrows=1)
        out = SAMPLES / name
        df.to_csv(out, index=False)
        print("wrote", out.name)


if __name__ == "__main__":
    main()
