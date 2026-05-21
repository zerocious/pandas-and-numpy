# Learning takeaways

Mistakes I hit while building these pipelines — and what I changed.

## 1. `SettingWithCopyWarning` and silent bugs

**What happened:** I filtered a DataFrame and assigned a new column without `.copy()`, so pandas warned (or updated a view unpredictably).

**Takeaway:** After `df[mask]`, call `.copy()` before adding columns. For subsets you edit, prefer `.loc` on a copy.

## 2. Dates parsed as strings or wrong year

**What happened:** `parse_dates=True` on `DD.MM.YYYY` strings gave wrong dtypes or empty filters. Filtering “2024” on `orders.csv` returned zero rows because data is **2023**.

**Takeaway:** Use `pd.to_datetime(..., format='%d.%m.%Y')` explicitly. Always check `df['date'].dtype` and `df['date'].dt.year.value_counts()` after parsing.

## 3. `agg` vs `transform` shape

**What happened:** I used `groupby().agg()` when I needed one value **per row** (e.g. category average for share). Result had wrong row count for downstream math.

**Takeaway:** Use **`transform`** when the output must align row-for-row with the source. Use **`agg`** when you want one row per group.

## 4. Merge keys that do not match

**What happened:** `user_id` formats differed (`U001` vs `U0001`) or no overlap → empty merges.

**Takeaway:** Cast keys to `str`, inspect `set(left) & set(right)`, use `validate='1:m'` to catch duplicate keys early.

## 5. `reset_index()` after groupby

**What happened:** Forgot `reset_index()` and could not access grouping columns as normal columns for export or further filters.

**Takeaway:** After `groupby().agg()`, call `reset_index()` (or use `as_index=False` in newer pandas) before filtering or `to_csv`.

---

Add your own notes below as you work through tasks.
