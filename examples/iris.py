from pandas import DataFrame,Series
import sys
import os
import math

sys.path.append(os.path.abspath(".."))

import ucc
import numpy as np

# The Iris Data Set is from the UCI Machine Learning Repository: http://archive.ics.uci.edu/ml/datasets/Iris


df = DataFrame.from_csv("iris.data",header = None,index_col = None, parse_dates = False)
df.columns = ['sepal_length','sepal_width','petal_length','petal_width','class']

df = df.dropna()

classNum = [1 if x == 'Iris-setosa' else 2 if x == 'Iris-versicolor' else 3 for x in df['class']]
df['classNum'] = classNum


u = ucc.UCC(df,columns=['sepal_length','sepal_width','petal_length','petal_width','classNum'])

print u.computeUCC().sort(['ucc'],ascending=False)