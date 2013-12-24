from pandas import DataFrame,Series
import sys
import os
import math

sys.path.append(os.path.abspath(".."))

import ucc
import numpy as np


x = Series(2 * math.pi * np.random.rand(1000))
y = np.vectorize(math.sin)(x) 

df = DataFrame({'x':x,'y':y})

print ucc.ucc(df)