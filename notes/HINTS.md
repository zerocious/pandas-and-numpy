# Task hints & advice

Use this when you're stuck. These are **nudges**, not full solutions — try the task first, then read one section at a time.

**Related files:** solution notebooks (`01-numpy.ipynb`, …), [PROGRESS.md](PROGRESS.md), [mistakes.md](mistakes.md)

### Quick index (29 tasks)

| Notebook | Tasks covered in this file |
|----------|----------------------------|
| `01-numpy-tasks` | 1.1–1.3, 2.1–2.3, 3.1–3.3, Boss fight |
| `02-pandas-fundamentals-tasks` | 5.1–5.3, 6.1–6.3, 7.1–7.3 |
| `03-pandas-pipelines-tasks` | Users/orders pipeline, High-impact quarters, Cohort retention, Events, Regional activity, Cohort dashboard |
| `04-pandas-business-tasks` | Regional sales audit, Customer 360, Churn risk, Channel concentration |

---

## 01 — NumPy (`01-numpy-tasks.ipynb`)

### Задание 1.1 — Arrays & attributes

- `np.array([...])` builds from a list; attributes are **properties**: `arr.shape`, `arr.ndim`, `arr.size`, `arr.dtype` (no parentheses).
- `np.ones((3, 4))` — shape is a **tuple**; `np.full((2, 5), 7.5)` fills with one value.
- `np.arange(0, 15, 2)` — stop is **exclusive** (like Python `range`).

**Stuck?** Print each result on its own line so you can match the expected output format.

---

### Задание 1.2 — Reshape & views

- `np.arange(0, 24)` then `.reshape(4, 6)` — total elements must match (24 = 4×6).
- For 3D with `-1`: `arr.reshape(2, 3, 4)` or `arr.reshape(-1, 3, 4)` — only **one** dimension can be `-1`.
- `ravel()` returns a **view** when possible → changing an element can change the original.
- `flatten()` always returns a **copy** → original stays unchanged.

**Stuck?** After step 4 with `ravel`, print `arr` again before resetting, to see the mutation.

---

### Задание 1.3 — dtype & memory

- `np.random.uniform(low, high, size=10_000)` — check `arr.dtype` and `arr.nbytes` before and after `.astype(np.float32)`.
- Memory halves roughly when float64 → float32 (same number of elements).
- `np.round(arr, 2)` or `np.round(arr, decimals=2, out=arr)` rounds in place.
- Final shape: `.reshape(250, 40)` — 250×40 = 10_000.

**Stuck?** Compare `arr.nbytes` with a calculator: `arr.size * arr.dtype.itemsize`.

---

### Задание 2.1 — Slicing & masks

- `np.arange(1, 31)` gives 1…30 (31 is exclusive).
- Slice 10th–20th **inclusive**: index 9 through 20 → `arr[9:21]`.
- Even mask: `(arr % 2 == 0)` — use the mask to **select**, not only to print.
- In-place replace: `arr[arr < 15] = -1`.

---

### Задание 2.2 — np.where & indices

- Random integers: `np.random.randint(10, 91, size=(5, 5))` (high is exclusive).
- Nested `np.where(cond, val_if_true, val_if_false)` or `np.select([cond1, cond2], [v1, v2], default=...)`.
- Indices of 100: `np.argwhere(arr == 100)` or `np.where(arr == 100)`.
- Last column to zero: `arr[:, -1] = 0`.

---

### Задание 2.3 — Filter & segments

- Column 0: `np.random.normal(500, 200, 1000)`; column 1: integers 1–10; column 2: 0/1 (e.g. `np.random.randint(0, 2, 1000)`).
- Combined filter: `(matrix[:, 0] > 800) & (matrix[:, 2] == 0)` — use `&`, not `and`.
- Share: `filtered_rows / len(matrix)` or `np.mean(mask)`.
- Segments: chain `np.where` or build a string array with `np.select`.
- Adding strings to a numeric matrix → **dtype=object** (mixed types).

---

### Задание 3.1 — Broadcasting

- Row-wise add: `matrix + np.array([1, 2, 3, 4, 5])` — shapes `(4,5)` and `(5,)`.
- Column-wise: reshape to `(4, 1)` or use `[:, np.newaxis]` so lengths align on the correct axis.
- Multiply by scalar max: `matrix * matrix.max()` (one number broadcasts everywhere).

**Stuck on ValueError?** Draw shapes on paper: `(4,5)` vs `(4,)` vs `(4,1)`.

---

### Задание 3.2 — Vectorization vs loop

- `np.random.randn(1_000_000)` for N(0,1).
- Time with `%timeit` in Jupyter or `time.perf_counter()` around the block.
- Vector form: `np.where(arr > 0, arr**2, np.abs(arr))` — no Python `for` over elements.
- Ratio `time_loop / time_vec` should be **much** larger than 1.

---

### Задание 3.3 — Min–max normalization

- `data = np.random.rand(1000, 5) * scale` — keep values positive so min–max is stable.
- `col_min = data.min(axis=0)`; `col_max = data.max(axis=0)` — axis=0 is **down columns**.
- Formula: `(data - col_min) / (col_max - col_min)` — broadcasting applies min/max per column.
- Check: `normalized.min(axis=0)`, `normalized.max(axis=0)` ≈ 0 and 1.

---

### Boss fight — Day 1 vector pipeline

Work in order; each step uses the result of the previous.

1. **Clip:** `np.nanpercentile(col, 95)` per column; `np.where(arr > p95, p95, arr)` — keep NaN with `np.where` + `np.isnan` or clip only non-NaN cells.
2. **Impute:** `np.nanmedian(arr, axis=0)` then fill NaNs (e.g. `np.where(np.isnan(arr), median, arr)`).
3. **Segments:** build boolean masks in priority order (VIP → Active → AtRisk → Standard); use `np.select`.
4. **Normalize:** same min–max as 3.3 on all 4 numeric columns.

**Stuck?** Generate synthetic data once with `np.random` + inject some NaN with boolean indexing. No `for` over rows — only over the 4 columns if needed for percentiles.

---

## 02 — Pandas fundamentals (`02-pandas-fundamentals-tasks.ipynb`)

### Задание 5.1 — DataFrame basics

- `pd.DataFrame({...})` from a dict of columns.
- `df.info()` shows dtypes and non-null counts.
- `astype`: `user_id` → `str`, `status` → `category`.
- Filter: `df[(df['status'] == 'active') & (df['revenue'] > 200)]`.
- Column subset: `df[['user_id', 'revenue']]` — double brackets.

---

### Задание 5.2 — loc / iloc

- Build with `pd.DataFrame(..., index=[...], columns=[...])` or `np.arange(1,16).reshape(5,3)`.
- `.loc['C', 'y'] = 999` — label-based.
- `.iloc[-1] = 0` — last row by position.
- Subset + **`.copy()`** before changing `z`, or you get `SettingWithCopyWarning` and may mutate the original.

---

### Задание 5.3 — Cleaning pipeline

- `f'ORD-{i:04d}'` for IDs; dates as strings `'DD.MM.YYYY'`.
- Parse: `pd.to_datetime(df['date_str'], format='%d.%m.%Y')`.
- Year filter: `df['date'].dt.year == 2024`.
- `fillna(0)` then `df[df['amount'] >= 0]`.
- `np.where(df['amount'] > 5000, 'High', 'Low')`.
- Save: `df.to_csv(str(OUT / 'clean_orders.csv'), index=False)`.

**Stuck?** Do dates first, then filter — easier to debug step by step.

---

### Задание 6.1 — groupby + agg

- Single agg: `df.groupby('category')['sales'].sum()`.
- Multiple: `.agg(['sum', 'mean'])` or named: `.agg(total_sales=('sales', 'sum'), avg_sales=('sales', 'mean'))`.
- Named syntax gives flat column names immediately.

---

### Задание 6.2 — Business metrics per region

- `groupby('region').agg(total_revenue=('order_amount', 'sum'), ... completed_orders=('is_completed', 'sum'), ...)`.
- `True` sums as 1 in pandas — good for counting completed orders.
- Filter **after** groupby: `result[result['total_orders'] >= 50]`.
- `reset_index()` so `region` becomes a column.

---

### Задание 6.3 — transform

- `groupby('category')['monthly_spend'].transform('mean')` — same row count as original.
- `spend_share = monthly_spend / category_avg_spend`.
- Boolean: `monthly_spend > category_avg_spend * 1.5`.
- Do **not** use `agg` here — you need one value per row.

---

### Задание 7.1 — merge

- `pd.merge(df_users, df_orders, on='user_id', how='left', validate='1:m')` — one user, many orders.
- `validate` catches duplicate keys early.
- `amount.fillna(0)` then `groupby('tier')['amount'].sum()`.

---

### Задание 7.2 — concat + pivot

- Tag each quarter before concat, or use `keys=['Q1','Q2','Q3']` in `pd.concat`.
- `pivot_table(index='region', columns='quarter', values='sales', aggfunc='sum', fill_value=0)`.
- New column: `df['Q3'] - df['Q2']` on the pivoted frame.

---

### Задание 7.3 — melt + share

- `pd.melt(df_wide, id_vars=['city'], value_vars=[...], var_name='month', value_name='revenue')`.
- Share: `df.groupby('city')['revenue'].transform('sum')` then divide.
- Filter: `df[df['share'] > 0.35]`.

---

## 03 — Pandas pipelines (`03-pandas-pipelines-tasks.ipynb`)

### Pipeline: users + orders → metrics_by_region

- Paths: `str(RAW / 'users.csv')`, save to `str(OUT / 'metrics_by_region.csv')`.
- **Dates:** `pd.to_datetime(..., format='%d.%m.%Y')` — avoid `parse_dates=True` on `DD.MM.YYYY` strings (pandas may mis-parse).
- `merge(..., how='left', validate='1:m')` — users without orders keep rows with NaN dates/amounts.
- **Year filter:** task text may say 2024, but `orders.csv` is **2023** — use `.dt.year == 2023` or you get an empty result.
- Filter year **after** merge; `fillna(0)` on amount for users with no orders.
- Active users: filter `amount > 0`, then `groupby('region').agg(..., active_users=('user_id', 'nunique'))`.
- `revenue_share = total_revenue / total_revenue.sum()`.

**Stuck?** Check `merged['order_date'].dtype` is datetime and `merged['user_id'].nunique()` before groupby.

---

### High-impact quarters (sales_wide)

> **Note:** In the notebook this block is titled «Когортный анализ…», but the work uses **`sales_wide.csv`** (melt + pivot), not `transactions.csv`.

- `pd.read_csv(str(RAW / 'sales_wide.csv'))` then `melt` with `id_vars=['product','region']`, quarter columns as `value_vars`.
- `total_year = groupby(['product','region'])['revenue'].transform('sum')`.
- Filter: `revenue > 0.35 * total_year`.
- `pivot_table(index='product', columns='quarter', values='revenue', aggfunc='sum').fillna(0)`.

---

### Cohort retention (transactions)

- Load with `dtype={'user_id': 'str'}`, parse dates.
- Drop `amount <= 0` first.
- Cohort month: `groupby('user_id')['transaction_date'].transform('min')` then `.dt.strftime('%Y-%m')`.
- Tx month: `transaction_date.dt.strftime('%Y-%m')`.
- `groupby(['cohort', 'tx_month']).agg(active_users=('user_id', 'nunique'))`.
- `cohort_size` via `transform` on first month of each cohort; `retention_rate = active_users / cohort_size`.
- Month diff: arithmetic on year/month — **no** merge.

**Stuck on month 0 = 100% retention?** Cohort size should come from users active in their **first** cohort month.

---

### Event metrics (raw_events)

- `read_csv` with `dtype={'user_id': 'str', 'value': 'float32'}`.
- `pd.to_datetime(..., format='%d.%m.%Y')`.
- `drop_duplicates(subset=['event_id'], keep='first')`.
- Median impute: `df.groupby('event_type')['value'].transform('median')` then `fillna` with that.
- Filter `event_date.dt.year == 2023`.
- `groupby('event_type').agg(...)`; `share_of_total = total_value / total_value.sum()`.
- Export: `index=False`, `encoding='utf-8-sig'` for Excel.

---

### Regional activity (users + sessions)

- Parse **both** date columns with `format='%d.%m.%Y'`.
- Clean sessions: drop `duration_sec <= 0`, `fillna(0)`.
- `merge` users ← sessions, `validate='1:m'`.
- `user_tenure_days = (session_date - signup_date).dt.days`.
- Filter rows with `duration_sec > 0` before aggregating if the task requires “active” sessions only.
- `groupby('region').agg(..., active_users=('user_id', 'nunique'))`.

---

### Cohort dashboard (transactions + pivot)

- Dedupe: `drop_duplicates(subset=['user_id', 'transaction_date'])`.
- Build cohort / tx_month like retention task.
- `groupby(['cohort', 'tx_month']).agg(revenue=('amount', 'sum'), buyers=('user_id', 'nunique'))`.
- `month_diff` from year/month subtraction (same formula as retention task).
- `cohort_revenue` at month 0: filter or `transform` on sorted data.
- `pivot_table(index='cohort', columns='month_diff', values='revenue_retention', fill_value=0)`.

---

## 04 — Pandas business (`04-pandas-business-tasks.ipynb`)

### Regional sales audit

- Input: `regional_sales_wide.csv` — wide monthly columns.
- `melt` → compute share per product–region with `transform('sum')`.
- Filter share > 0.22 (task threshold).
- `pivot_table` for summary matrix (product × region).
- `str(OUT / 'Regional_Sales_Audit_Summary.csv')`.

**Stuck?** Do melt first, then shares on long data — don't try to compute shares on wide format.

---

### Customer 360 (crm + billing)

- `dtype={'cust_id': str}` on both files; `drop_duplicates` on CRM.
- Billing stats: `groupby('cust_id').agg(total_invoices=(..., 'count'), max_invoice_amount=(..., 'max'))`.
- `merge(crm, billing, on='cust_id', how='left')` — keep all customers.
- Regional median signup: `groupby('region')['signup_date'].transform('median')` then `fillna`.
- `np.where(max_invoice_amount > 200, ...)` for `is_high_value` (watch NaN → False or fill first).

---

### Churn risk (user_events)

Break into small cells:

1. Load + `pd.to_datetime(event_date)`.
2. Sort `['user_id', 'event_date']`.
3. Session breaks: `(df.groupby('user_id')['event_date'].diff() > pd.Timedelta('30min')).cumsum()` (+ groupby user for independent counters).
4. Per session: `groupby('session_id').agg(session_duration=..., event_count=...)`.
5. `user_global_avg_duration` via `groupby('user_id').transform('mean')`.
6. Monthly average duration → compare to 70% of global baseline.
7. Keep users with `nunique` months >= 3.

**Stuck on sessions?** Draw 5 events on a timeline; mark gaps > 30 min — each gap starts a new session.

**Avoid:** `apply` and `merge` — use `transform` to broadcast baselines.

---

### Channel concentration

1. `melt` channel columns to long; drop `revenue == 0` or NaN; count dropped rows.
2. Three shares — all via `transform('sum')` on different group keys:
   - by `product`, by `channel`, and divide by the **grand total** for `share_of_total`.
3. **HHI (no lambda, no apply):** square shares, then sum within product:
   `df['hhi_product'] = (df['share_of_product'] ** 2).groupby(df['product']).transform('sum')`
4. `risk_class` with `np.select` (thresholds: 0.35, 0.10).
5. Product summary: `groupby('product').agg(...)` + `idxmax` pattern from the task notebook.
6. Two CSV exports: `channel_pairs_long.csv`, `product_concentration_summary.csv`.

---

## General tips

| Problem | Try |
|--------|-----|
| `SettingWithCopyWarning` | Add `.copy()` after filtering before assigning columns |
| Dates wrong / empty filter | Use explicit `format='%d.%m.%Y'`, check `.dtype` |
| Merge gives too few rows | Check `user_id` formats match (`str`), key overlap |
| `validate` fails | Duplicates in left key — `drop_duplicates` first |
| Groupby wrong shape | Use `transform` not `agg` when you need one row per input row |
| Excel garbled Cyrillic | `encoding='utf-8-sig'` on export |

When hints aren't enough, open the matching **solution notebook** for one cell only, then close it and retry from memory.
