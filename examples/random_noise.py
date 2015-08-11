import sys

sys.path = ['..'] + sys.path

import numpy as np

from pandas import DataFrame
from ucc_pandas import UCC

x = np.random.rand(1000)
y = np.random.rand(1000)

df = DataFrame({'x': x, 'y': y})

ucc = UCC(df)

print(ucc.compute_ucc())
