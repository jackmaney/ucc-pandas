import sys

sys.path = ['..'] + sys.path

import math
from ucc_pandas import UCC

from pandas import DataFrame, Series

import numpy as np

x = Series(2 * math.pi * np.random.rand(1000))
y = np.vectorize(math.sin)(x) 

df = DataFrame(dict(x=x, y=y))

ucc = UCC(df)

print(ucc.compute_ucc())
