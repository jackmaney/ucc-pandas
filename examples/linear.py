import sys

sys.path = ['..'] + sys.path

from pandas import DataFrame, Series

from ucc_pandas import UCC

x = Series(list(range(1, 1001)))
y = (3 * x) + 1

df = DataFrame({'x': x, 'y': y})

ucc = UCC(df)

print(ucc.compute_ucc())
