# Task hints & advice

Nudges when you are stuck — not full solutions.

Russian: [HINTS.ru.md](HINTS.ru.md)

### Jump navigation

**01 — NumPy:** [1.1](#task-11) · [1.2](#task-12) · [1.3](#task-13) · [2.1](#task-21) · [2.2](#task-22) · [2.3](#task-23) · [3.1](#task-31) · [3.2](#task-32) · [3.3](#task-33) · [Boss](#boss-1)

**02 — Pandas fundamentals:** [5.1](#task-51) · [5.2](#task-52) · [5.3](#task-53) · [6.1](#task-61) · [6.2](#task-62) · [6.3](#task-63) · [7.1](#task-71) · [7.2](#task-72) · [7.3](#task-73)

**03 — Pipelines:** [Users/orders](#pipeline-1) · [Quarters](#pipeline-2) · [Cohort](#pipeline-3) · [Events](#pipeline-4) · [Regional](#pipeline-5) · [Dashboard](#pipeline-6)

**04 — Business:** [Sales](#business-1) · [Customer 360](#business-2) · [Churn](#business-3) · [Channels](#business-4)

**Other:** [General tips](#general-tips)

---

---

<a id="numpy"></a>

## 01 тАФ NumPy (`01-numpy-tasks.ipynb`)

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-11"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 1.1 тАФ Arrays & attributes

- `np.array([...])` builds from a list; attributes are **properties**: `arr.shape`, `arr.ndim`, `arr.size`, `arr.dtype` (no parentheses).
- `np.ones((3, 4))` тАФ shape is a **tuple**; `np.full((2, 5), 7.5)` fills with one value.
- `np.arange(0, 15, 2)` тАФ stop is **exclusive** (like Python `range`).

**Stuck?** Print each result on its own line so you can match the expected output format.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-12"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 1.2 тАФ Reshape & views

- `np.arange(0, 24)` then `.reshape(4, 6)` тАФ total elements must match (24 = 4├Ч6).
- For 3D with `-1`: `arr.reshape(2, 3, 4)` or `arr.reshape(-1, 3, 4)` тАФ only **one** dimension can be `-1`.
- `ravel()` returns a **view** when possible тЖТ changing an element can change the original.
- `flatten()` always returns a **copy** тЖТ original stays unchanged.

**Stuck?** After step 4 with `ravel`, print `arr` again before resetting, to see the mutation.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-13"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 1.3 тАФ dtype & memory

- `np.random.uniform(low, high, size=10_000)` тАФ check `arr.dtype` and `arr.nbytes` before and after `.astype(np.float32)`.
- Memory halves roughly when float64 тЖТ float32 (same number of elements).
- `np.round(arr, 2)` or `np.round(arr, decimals=2, out=arr)` rounds in place.
- Final shape: `.reshape(250, 40)` тАФ 250├Ч40 = 10_000.

**Stuck?** Compare `arr.nbytes` with a calculator: `arr.size * arr.dtype.itemsize`.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-21"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 2.1 тАФ Slicing & masks

- `np.arange(1, 31)` gives 1тАж30 (31 is exclusive).
- Slice 10thтАУ20th **inclusive**: index 9 through 20 тЖТ `arr[9:21]`.
- Even mask: `(arr % 2 == 0)` тАФ use the mask to **select**, not only to print.
- In-place replace: `arr[arr < 15] = -1`.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-22"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 2.2 тАФ np.where & indices

- Random integers: `np.random.randint(10, 91, size=(5, 5))` (high is exclusive).
- Nested `np.where(cond, val_if_true, val_if_false)` or `np.select([cond1, cond2], [v1, v2], default=...)`.
- Indices of 100: `np.argwhere(arr == 100)` or `np.where(arr == 100)`.
- Last column to zero: `arr[:, -1] = 0`.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-23"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 2.3 тАФ Filter & segments

- Column 0: `np.random.normal(500, 200, 1000)`; column 1: integers 1тАУ10; column 2: 0/1 (e.g. `np.random.randint(0, 2, 1000)`).
- Combined filter: `(matrix[:, 0] > 800) & (matrix[:, 2] == 0)` тАФ use `&`, not `and`.
- Share: `filtered_rows / len(matrix)` or `np.mean(mask)`.
- Segments: chain `np.where` or build a string array with `np.select`.
- Adding strings to a numeric matrix тЖТ **dtype=object** (mixed types).

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-31"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 3.1 тАФ Broadcasting

- Row-wise add: `matrix + np.array([1, 2, 3, 4, 5])` тАФ shapes `(4,5)` and `(5,)`.
- Column-wise: reshape to `(4, 1)` or use `[:, np.newaxis]` so lengths align on the correct axis.
- Multiply by scalar max: `matrix * matrix.max()` (one number broadcasts everywhere).

**Stuck on ValueError?** Draw shapes on paper: `(4,5)` vs `(4,)` vs `(4,1)`.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-32"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 3.2 тАФ Vectorization vs loop

- `np.random.randn(1_000_000)` for N(0,1).
- Time with `%timeit` in Jupyter or `time.perf_counter()` around the block.
- Vector form: `np.where(arr > 0, arr**2, np.abs(arr))` тАФ no Python `for` over elements.
- Ratio `time_loop / time_vec` should be **much** larger than 1.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-33"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 3.3 тАФ MinтАУmax normalization

- `data = np.random.rand(1000, 5) * scale` тАФ keep values positive so minтАУmax is stable.
- `col_min = data.min(axis=0)`; `col_max = data.max(axis=0)` тАФ axis=0 is **down columns**.
- Formula: `(data - col_min) / (col_max - col_min)` тАФ broadcasting applies min/max per column.
- Check: `normalized.min(axis=0)`, `normalized.max(axis=0)` тЙИ 0 and 1.

---

<a id="boss-1"></a>

### Boss fight тАФ Day 1 vector pipeline

Work in order; each step uses the result of the previous.

1. **Clip:** `np.nanpercentile(col, 95)` per column; `np.where(arr > p95, p95, arr)` тАФ keep NaN with `np.where` + `np.isnan` or clip only non-NaN cells.
2. **Impute:** `np.nanmedian(arr, axis=0)` then fill NaNs (e.g. `np.where(np.isnan(arr), median, arr)`).
3. **Segments:** build boolean masks in priority order (VIP тЖТ Active тЖТ AtRisk тЖТ Standard); use `np.select`.
4. **Normalize:** same minтАУmax as 3.3 on all 4 numeric columns.

**Stuck?** Generate synthetic data once with `np.random` + inject some NaN with boolean indexing. No `for` over rows тАФ only over the 4 columns if needed for percentiles.

---

<a id="pandas-fundamentals"></a>

## 02 тАФ Pandas fundamentals (`02-pandas-fundamentals-tasks.ipynb`)

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-51"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 5.1 тАФ DataFrame basics

- `pd.DataFrame({...})` from a dict of columns.
- `df.info()` shows dtypes and non-null counts.
- `astype`: `user_id` тЖТ `str`, `status` тЖТ `category`.
- Filter: `df[(df['status'] == 'active') & (df['revenue'] > 200)]`.
- Column subset: `df[['user_id', 'revenue']]` тАФ double brackets.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-52"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 5.2 тАФ loc / iloc

- Build with `pd.DataFrame(..., index=[...], columns=[...])` or `np.arange(1,16).reshape(5,3)`.
- `.loc['C', 'y'] = 999` тАФ label-based.
- `.iloc[-1] = 0` тАФ last row by position.
- Subset + **`.copy()`** before changing `z`, or you get `SettingWithCopyWarning` and may mutate the original.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-53"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 5.3 тАФ Cleaning pipeline

- `f'ORD-{i:04d}'` for IDs; dates as strings `'DD.MM.YYYY'`.
- Parse: `pd.to_datetime(df['date_str'], format='%d.%m.%Y')`.
- Year filter: `df['date'].dt.year == 2024`.
- `fillna(0)` then `df[df['amount'] >= 0]`.
- `np.where(df['amount'] > 5000, 'High', 'Low')`.
- Save: `df.to_csv(str(OUT / 'clean_orders.csv'), index=False)`.

**Stuck?** Do dates first, then filter тАФ easier to debug step by step.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-61"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 6.1 тАФ groupby + agg

- Single agg: `df.groupby('category')['sales'].sum()`.
- Multiple: `.agg(['sum', 'mean'])` or named: `.agg(total_sales=('sales', 'sum'), avg_sales=('sales', 'mean'))`.
- Named syntax gives flat column names immediately.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-62"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 6.2 тАФ Business metrics per region

- `groupby('region').agg(total_revenue=('order_amount', 'sum'), ... completed_orders=('is_completed', 'sum'), ...)`.
- `True` sums as 1 in pandas тАФ good for counting completed orders.
- Filter **after** groupby: `result[result['total_orders'] >= 50]`.
- `reset_index()` so `region` becomes a column.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-63"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 6.3 тАФ transform

- `groupby('category')['monthly_spend'].transform('mean')` тАФ same row count as original.
- `spend_share = monthly_spend / category_avg_spend`.
- Boolean: `monthly_spend > category_avg_spend * 1.5`.
- Do **not** use `agg` here тАФ you need one value per row.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-71"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 7.1 тАФ merge

- `pd.merge(df_users, df_orders, on='user_id', how='left', validate='1:m')` тАФ one user, many orders.
- `validate` catches duplicate keys early.
- `amount.fillna(0)` then `groupby('tier')['amount'].sum()`.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-72"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 7.2 тАФ concat + pivot

- Tag each quarter before concat, or use `keys=['Q1','Q2','Q3']` in `pd.concat`.
- `pivot_table(index='region', columns='quarter', values='sales', aggfunc='sum', fill_value=0)`.
- New column: `df['Q3'] - df['Q2']` on the pivoted frame.

---

<a id="╨╖╨░╨┤╨░╨╜╨╕╨╡-73"></a>

### ╨Ч╨░╨┤╨░╨╜╨╕╨╡ 7.3 тАФ melt + share

- `pd.melt(df_wide, id_vars=['city'], value_vars=[...], var_name='month', value_name='revenue')`.
- Share: `df.groupby('city')['revenue'].transform('sum')` then divide.
- Filter: `df[df['share'] > 0.35]`.

---

<a id="pandas-pipelines"></a>

## 03 тАФ Pandas pipelines (`03-pandas-pipelines-tasks.ipynb`)

<a id="pipeline-1"></a>

### Pipeline: users + orders тЖТ metrics_by_region

- Paths: `str(RAW / 'users.csv')`, save to `str(OUT / 'metrics_by_region.csv')`.
- **Dates:** `pd.to_datetime(..., format='%d.%m.%Y')` тАФ avoid `parse_dates=True` on `DD.MM.YYYY` strings (pandas may mis-parse).
- `merge(..., how='left', validate='1:m')` тАФ users without orders keep rows with NaN dates/amounts.
- **Year filter:** use `.dt.year == 2023` (matches `orders.csv`).
- Filter year **after** merge; `fillna(0)` on amount for users with no orders.
- Active users: filter `amount > 0`, then `groupby('region').agg(..., active_users=('user_id', 'nunique'))`.
- `revenue_share = total_revenue / total_revenue.sum()`.

**Stuck?** Check `merged['order_date'].dtype` is datetime and `merged['user_id'].nunique()` before groupby.

---

<a id="pipeline-2"></a>

### High-impact quarters (sales_wide)

- `pd.read_csv(str(RAW / 'sales_wide.csv'))` then `melt` with `id_vars=['product','region']`, quarter columns as `value_vars`.
- `total_year = groupby(['product','region'])['revenue'].transform('sum')`.
- Filter: `revenue > 0.35 * total_year`.
- `pivot_table(index='product', columns='quarter', values='revenue', aggfunc='sum').fillna(0)`.

---

<a id="pipeline-3"></a>

### Cohort retention (transactions)

- Load with `dtype={'user_id': 'str'}`, parse dates.
- Drop `amount <= 0` first.
- Cohort month: `groupby('user_id')['transaction_date'].transform('min')` then `.dt.strftime('%Y-%m')`.
- Tx month: `transaction_date.dt.strftime('%Y-%m')`.
- `groupby(['cohort', 'tx_month']).agg(active_users=('user_id', 'nunique'))`.
- `cohort_size` via `transform` on first month of each cohort; `retention_rate = active_users / cohort_size`.
- Month diff: arithmetic on year/month тАФ **no** merge.

**Stuck on month 0 = 100% retention?** Cohort size should come from users active in their **first** cohort month.

---

<a id="pipeline-4"></a>

### Event metrics (raw_events)

- `read_csv` with `dtype={'user_id': 'str', 'value': 'float32'}`.
- `pd.to_datetime(..., format='%d.%m.%Y')`.
- `drop_duplicates(subset=['event_id'], keep='first')`.
- Median impute: `df.groupby('event_type')['value'].transform('median')` then `fillna` with that.
- Filter `event_date.dt.year == 2023`.
- `groupby('event_type').agg(...)`; `share_of_total = total_value / total_value.sum()`.
- Export: `index=False`, `encoding='utf-8-sig'` for Excel.

---

<a id="pipeline-5"></a>

### Regional activity (users + sessions)

- Parse **both** date columns with `format='%d.%m.%Y'`.
- Clean sessions: drop `duration_sec <= 0`, `fillna(0)`.
- `merge` users тЖР sessions, `validate='1:m'`.
- `user_tenure_days = (session_date - signup_date).dt.days`.
- Filter rows with `duration_sec > 0` before aggregating if the task requires тАЬactiveтАЭ sessions only.
- `groupby('region').agg(..., active_users=('user_id', 'nunique'))`.

---

<a id="pipeline-6"></a>

### Cohort dashboard (transactions + pivot)

- Dedupe: `drop_duplicates(subset=['user_id', 'transaction_date'])`.
- Build cohort / tx_month like retention task.
- `groupby(['cohort', 'tx_month']).agg(revenue=('amount', 'sum'), buyers=('user_id', 'nunique'))`.
- `month_diff` from year/month subtraction (same formula as retention task).
- `cohort_revenue` at month 0: filter or `transform` on sorted data.
- `pivot_table(index='cohort', columns='month_diff', values='revenue_retention', fill_value=0)`.

---

<a id="pandas-business"></a>

## 04 тАФ Pandas business (`04-pandas-business-tasks.ipynb`)

<a id="business-1"></a>

### Regional sales audit

- Input: `regional_sales_wide.csv` тАФ wide monthly columns.
- `melt` тЖТ compute share per productтАУregion with `transform('sum')`.
- Filter share > 0.22 (task threshold).
- `pivot_table` for summary matrix (product ├Ч region).
- `str(OUT / 'Regional_Sales_Audit_Summary.csv')`.

**Stuck?** Do melt first, then shares on long data тАФ don't try to compute shares on wide format.

---

<a id="business-2"></a>

### Customer 360 (crm + billing)

- `dtype={'cust_id': str}` on both files; `drop_duplicates` on CRM.
- Billing stats: `groupby('cust_id').agg(total_invoices=(..., 'count'), max_invoice_amount=(..., 'max'))`.
- `merge(crm, billing, on='cust_id', how='left')` тАФ keep all customers.
- Regional median signup: `groupby('region')['signup_date'].transform('median')` then `fillna`.
- `np.where(max_invoice_amount > 200, ...)` for `is_high_value` (watch NaN тЖТ False or fill first).

---

<a id="business-3"></a>

### Churn risk (user_events)

Break into small cells:

1. Load + `pd.to_datetime(event_date)`.
2. Sort `['user_id', 'event_date']`.
3. Session breaks: `(df.groupby('user_id')['event_date'].diff() > pd.Timedelta('30min')).cumsum()` (+ groupby user for independent counters).
4. Per session: `groupby('session_id').agg(session_duration=..., event_count=...)`.
5. `user_global_avg_duration` via `groupby('user_id').transform('mean')`.
6. Monthly average duration тЖТ compare to 70% of global baseline.
7. Keep users with `nunique` months >= 3.

**Stuck on sessions?** Draw 5 events on a timeline; mark gaps > 30 min тАФ each gap starts a new session.

**Avoid:** `apply` and `merge` тАФ use `transform` to broadcast baselines.

---

<a id="business-4"></a>

### Channel concentration

1. `melt` channel columns to long; drop `revenue == 0` or NaN; count dropped rows.
2. Three shares тАФ all via `transform('sum')` on different group keys:
   - by `product`, by `channel`, and divide by the **grand total** for `share_of_total`.
3. **HHI (no lambda, no apply):** square shares, then sum within product:
   `df['hhi_product'] = (df['share_of_product'] ** 2).groupby(df['product']).transform('sum')`
4. `risk_class` with `np.select` (thresholds: 0.35, 0.10).
5. Product summary: `groupby('product').agg(...)` + `idxmax` pattern from the task notebook.
6. Two CSV exports: `channel_pairs_long.csv`, `product_concentration_summary.csv`.

---

<a id="general-tips"></a>

## General tips

| Problem | Try |
|--------|-----|
| `SettingWithCopyWarning` | Add `.copy()` after filtering before assigning columns |
| Dates wrong / empty filter | Use explicit `format='%d.%m.%Y'`, check `.dtype` |
| Merge gives too few rows | Check `user_id` formats match (`str`), key overlap |
| `validate` fails | Duplicates in left key тАФ `drop_duplicates` first |
| Groupby wrong shape | Use `transform` not `agg` when you need one row per input row |
| Excel garbled Cyrillic | `encoding='utf-8-sig'` on export |

When hints aren't enough, open the matching **solution notebook** for one cell only, then close it and retry from memory.
