from pandas import DataFrame,Series
import pandas as pd
import numpy as np
from numbers import Number

def __validate_and_grab_columns(data,x=None,y=None):
	if not isinstance(data,DataFrame):
		raise Exception("Data argument is not a pandas DataFrame")

	if data.shape[1] < 2:
		raise Exception("DataFrame must have at least two columns")

	xColumn = None
	yColumn = None

	if x is None:
		xColumn = data.columns[0]
	else:
		if x not in data.columns:
			raise Exception("Column %s not found in the given DataFrame" % x)
		xColumn = x

	if y is None:
		yColumn = data.columns[1]
	else:
		if y not in data.columns:
			raise Exception("Column %s not found in the given DataFrame" % y)
		yColumn = y

	for i in list(range(data.shape[0])):
		if not __is_actual_number(data[xColumn][i]) or not __is_actual_number(data[yColumn][i]): 
			raise Exception("Non-numeric values found at row %d (%s,%s)" % (i+1),data[xColumn][i],data[yColumn][i])

	return (xColumn,yColumn)

def __is_actual_number(x):
	return isinstance(x,Number) and not np.isnan(x)

def __trim(data,x,y):
	return data[[x,y]]

def __ucc_x(data,x,y):
	return np.ediff1d(data.sort([x]).rank()[y].values).mean()

def __ucc_y(data,x,y):
	return __ucc_x(data,y,x)

def ucc(data,x=None,y=None):
	columns = __validate_and_grab_columns(data,x=x,y=y)
	
	x = columns[0]
	y = columns[1]

	dataFrame = __trim(data,x,y).drop_duplicates

	ucc_x = __ucc_x(data,x,y)
	ucc_y = __ucc_y(data,x,y)
	ucc = max([ucc_x,ucc_y])

	return Series([ucc_x,ucc_y,ucc],index=['ucc_x','ucc_y','ucc'])
