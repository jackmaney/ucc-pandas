import sys

sys.path = ['..'] + sys.path

import math

from pandas import DataFrame
from ucc_pandas import UCC
import numpy as np
from math import factorial

x = 4 * math.pi * np.random.random_sample(10000) - 2 * math.pi

cosine = np.vectorize(math.cos)(x)

cos_noisy = cosine + (0.2 * np.random.random_sample(10000) - 0.1)

sine = np.vectorize(math.sin)(x)

sin_noisy = sine + (0.2 * np.random.random_sample(10000) - 0.1)

cos_approx = np.sum([((-1) ** i) * x ** i / factorial(i)
                     for i in range(0, 11, 2)], axis=0)

sin_approx = np.sum([((-1) ** i) * x ** i / factorial(i)
                     for i in range(1, 12, 2)], axis=0)

df = DataFrame(
    dict(x_squared=x ** 2, random=np.random.random_sample(10000),
         cosine=cosine, cos_approx=cos_approx, cos_noisy=cos_noisy,
         sine=sine, sin_approx=sin_approx, sin_noisy=sin_noisy))

ucc = UCC(df)

print(ucc.compute_ucc())
