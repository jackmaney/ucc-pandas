import sys

sys.path = ['..'] + sys.path
import os

from pandas import DataFrame

from ucc_pandas import UCC

# The Iris Data Set is from the UCI Machine Learning Repository: http://archive.ics.uci.edu/ml/datasets/Iris


df = DataFrame.from_csv("iris.data", header=None, index_col=None, parse_dates=False)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = df.dropna()

classNum = [1 if x == 'Iris-setosa' else 2 if x == 'Iris-versicolor' else 3 for x in df['class']]
df['classNum'] = classNum

ucc = UCC(df, columns=['sepal_length', 'sepal_width',
                       'petal_length', 'petal_width', 'classNum'])

print(ucc.compute_ucc().sort(['ucc'], ascending=False))
