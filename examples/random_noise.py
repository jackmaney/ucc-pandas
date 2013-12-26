from pandas import DataFrame,Series
import sys
import os
import math

sys.path.append(os.path.abspath(".."))

import ucc
import numpy as np


x = np.random.rand(1000)
y = np.random.rand(1000)

df = DataFrame({'x':x,'y':y})

u = ucc.UCC(df)

print u.computeUCC()