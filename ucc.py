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
			raise Exception("Non-numeric values found: (" + str(data[xColumn][i]) + "," + str(data[yColumn][i]) + ")")

	return (xColumn,yColumn)

def __is_actual_number(x):
	return np.isreal(x) and not np.isnan(x)

def __trim(data,x,y):
	return data[[x,y]]

def __avg_of_deltas(data,independent,dependent):
	return np.ediff1d(data.sort([independent]).rank()[dependent].values).mean()

def ucc(data,x=None,y=None,copy=False):
	columns = __validate_and_grab_columns(data,x=x,y=y)
	
	xColumn = columns[0]
	yColumn = columns[1]
	
	dataFrame = None
	
	if(copy):
		dataFrame = __trim(data,xColumn,yColumn).drop_duplicates
	else:
		dataFrame = data.drop_duplicates([xColumn,yColumn])
	
	n = dataFrame.shape[0]
	
	ucc_x = 1 - __avg_of_deltas(dataFrame,xColumn,yColumn) * 3 / n
	ucc_y = 1 - __avg_of_deltas(dataFrame,yColumn,xColumn) * 3 / n
	ucc = max([ucc_x,ucc_y])

	return Series([ucc_x,ucc_y,ucc],index=['ucc_x','ucc_y','ucc'])
