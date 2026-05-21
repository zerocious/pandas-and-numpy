# Data dictionary

Synthetic datasets for analytics exercises. Outputs in `output/` are **regenerated** by solution notebooks (not committed).

## Raw files (`raw/`)

| File | Rows (approx.) | Grain | Key columns | Quirks |
|------|----------------|-------|-------------|--------|
| `users.csv` | 150 | 1 row / user | `user_id`, `region`, `signup_date` | Dates as `DD.MM.YYYY` strings |
| `orders.csv` | 800 | 1 row / order | `order_id`, `user_id`, `order_date`, `amount` | Year **2023**; join keys align with `users` |
| `transactions.csv` | 509 | 1 row / txn | `user_id`, `transaction_date`, `amount`, `category` | Some negative amounts (cancellations) |
| `sessions.csv` | 800 | 1 row / session | `session_id`, `user_id`, `session_date`, `duration_sec` | Dates `DD.MM.YYYY`; some zero/negative duration |
| `raw_events.csv` | 2,025 | 1 row / event | `event_id`, `user_id`, `event_date`, `event_type`, `value` | Date `DD.MM.YYYY`; duplicate `event_id` possible; NaN in `value` |
| `sales_wide.csv` | 20 | product × region | `q1_rev`…`q4_rev` | Wide quarterly revenue |
| `regional_sales_wide.csv` | 20 | product × region | `Jan`…`Jun` | Wide monthly revenue |
| `channel_sales_wide.csv` | 5 | product × channel | channel columns as wide | Annual revenue by channel |
| `crm_raw.csv` | 5,150 | 1 row / customer | `cust_id`, `region`, `signup_date` | Duplicate `cust_id` possible |
| `billing_raw.csv` | 3,000 | 1 row / invoice | `cust_id`, `invoice_id`, `amount`, `status` | Not every CRM customer has invoices |
| `user_events.csv` | 170k | 1 row / event | `user_id`, `segment`, `event_date` | High volume; sessionization exercise |

## Generated outputs (`output/`)

| File | Produced by | Purpose |
|------|-------------|---------|
| `metrics_by_region.csv` | 03 pipelines | Regional revenue & active users |
| `high_impact_quarters.csv` | 03 pipelines | Quarters > 35% of annual pair revenue |
| `cohort_retention_real.csv` | 03 pipelines | Cohort retention rates |
| `event_metrics_2023.csv` | 03 pipelines | Event type KPIs + share of total |
| `regional_activity.csv` | 03 pipelines | Session metrics by region |
| `cohort_dashboard.csv` | 03 pipelines | Revenue retention pivot |
| `clean_orders.csv` | 02 fundamentals | Cleaned synthetic orders |
| `customer_master.csv` | 04 business | CRM + billing master |
| `churn_risk_analysis.csv` | 04 business | User-month engagement risk |
| `channel_pairs_long.csv` | 04 business | Channel mix & risk class |
| `product_concentration_summary.csv` | 04 business | HHI & top channel per product |
| `Regional_Sales_Audit_Summary.csv` | 04 business | Filtered sales summary matrix |

Sample rows (no full export): [../docs/samples/](../docs/samples/)
