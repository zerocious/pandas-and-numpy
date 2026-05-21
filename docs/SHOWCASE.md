# Portfolio showcase

Three pipelines that best represent the project for reviewers. Full code: solution notebooks in [`notebooks/`](../notebooks/).

---

## 1. Regional metrics pipeline

**Problem:** Marketing needs revenue and active-user counts by region from separate user and order logs.

**Approach:**
1. Load `users.csv` and `orders.csv` with explicit dtypes and `DD.MM.YYYY` parsing
2. `left` merge on `user_id` with `validate='1:m'`
3. Filter orders to **2023**, fill missing amounts with 0
4. Aggregate per `region`: sum, mean, `nunique` active users
5. Add `revenue_share` for each region

**Key pandas:** `pd.to_datetime`, `merge`, `groupby().agg()`, column arithmetic

**Output:** `metrics_by_region.csv`

| Column | Meaning |
|--------|---------|
| `total_revenue` | Sum of order amounts |
| `avg_order` | Mean order value |
| `active_users` | Users with amount > 0 |
| `revenue_share` | Region share of total revenue |

---

## 2. Cohort retention

**Problem:** Product wants retention in the first 6 months after each user's first purchase.

**Approach:**
1. Load `transactions.csv`, drop cancellations (`amount <= 0`)
2. Assign **cohort** = month of first purchase per user
3. Assign **tx_month** per transaction
4. Count `active_users` per `(cohort, tx_month)`
5. `retention_rate = active_users / cohort_size` (size from month 0)
6. Filter `cohort_size >= 20` and month offset 0–5

**Key pandas:** `transform('min')`, `strftime`, `groupby`, boolean filters — no merge

**Output:** `cohort_retention_real.csv`

| Column | Meaning |
|--------|---------|
| `cohort` | First-purchase month (YYYY-MM) |
| `tx_month` | Transaction month |
| `active_users` | Unique buyers |
| `cohort_size` | Users active in cohort month 0 |
| `retention_rate` | active_users / cohort_size |

---

## 3. Churn risk (sessionization)

**Problem:** Identify users whose **recent** engagement dropped vs their own historical baseline (not segment average).

**Approach:**
1. Load `user_events.csv`, parse `event_date`
2. Sort by user; new session when gap > **30 minutes** (`diff` + `cumsum`)
3. Aggregate session duration per session, then monthly average per user
4. Compare monthly average to **70%** of user's global average → `is_at_risk`
5. Keep users active in ≥ 3 months

**Key pandas:** `diff`, `Timedelta`, `groupby().transform()`, no `apply` on rows

**Output:** `churn_risk_analysis.csv`

| Column | Meaning |
|--------|---------|
| `user_id` | User |
| `event_date_month` | Month (YYYY-MM) |
| `monthly_avg_duration` | Avg session length that month |
| `user_global_avg_duration` | User's overall baseline |
| `is_at_risk` | True if monthly < 70% of baseline |

---

See [samples/](samples/) for example output rows.
