from pandas import DataFrame,Series
import sys
import os
import math

sys.path.append(os.path.abspath(".."))

import ucc
import numpy as np

x = 4 * math.pi * np.random.rand(10000) - 2 * math.pi

xSquared = x * x

xCubed = x * x * x

xFourth = x * x * x * x

xFifth = x * x * x * x * x

cosine = np.vectorize(math.cos)(x)

sine = np.vectorize(math.sin)(x)

cosApprox = 1 - (xSquared / 2) + (xFourth / 24)

sinApprox = x - (xCubed / 6) + (xFifth / 120)

df = DataFrame({'xSquared':xSquared,'xFourth':xFourth,'cosine':cosine,'cosApprox':cosApprox,'sine':sine,
	'sinApprox':sinApprox})

u = ucc.UCC(df)

print u.computeUCC()