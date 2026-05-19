Forgot to use df.reset_index(), couldn't use first two columns, used for grouping. (could also use as_index=False)
Didn't use 'aggfunc', instead of aggfunc to fasten the code.
Calculating 'mean', when the table isn't grouped properly. (1 row per value, that should be calculated with 'mean'. Otherwise the result will be wrong, as difference in rows will affect it.)
Trying to input unmatching dtypes in a column

