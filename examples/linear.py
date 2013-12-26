from pandas import DataFrame,Series
import sys
import os

sys.path.append(os.path.abspath(".."))

import ucc

x = Series(list(range(1,1001)))
y = 3 * x + 1

df = DataFrame({'x':x,'y':y})

u = ucc.UCC(df)

print(u.computeUCC())