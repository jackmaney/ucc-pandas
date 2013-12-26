from pandas import DataFrame,Series
import pandas as pd
import numpy as np
from numbers import Number

class UCC:

	def __init__(self,dataFrame,columns=None,x=None,y=None):
		if not isinstance(dataFrame,DataFrame):
			raise Exception("dataFrame argument is not a pandas DataFrame")
		elif dataFrame.empty:
			raise Exception("The given data frame is empty")
		elif dataFrame.shape[1] < 2:
			raise Exception("The given data frame must have at least two columns")

		self.dataFrame = dataFrame
		self.columns = None

		if x is not None and y is not None:
			self.columns = [x,y]
		elif columns is not None:
			self.columns = columns
		else:
			self.columns = dataFrame.columns

		self.__check_columns()

		self.dataFrame = self.dataFrame.drop_duplicates(columns)

	def __check_columns(self):
		if len(self.columns) < 2:
			raise Exception("At least two columns are required")

		for col in self.columns:
			if col not in self.dataFrame.columns:
				raise Exception("There is no column in the given data frame by the name of '%s'" % col)
			if not self.__is_numeric(col):
				raise Exception("The column '%s' is either not numeric or contains NaN values" % col)

	def __is_numeric(self,col):
		return all(np.isreal(self.dataFrame[col])) and not any(np.isnan(self.dataFrame[col]))

	def __avg_of_abs_deltas(self,independent,dependent):
		"""
		This could be done in a way that's more easy to read, but I wanted to use the
		built-in functionality in pandas and numpy. So, unwrapping this from the inside out:

		* self.dataFrame.sort([independent]): sorts our data by the column name for the 
			independent variable.

		* .rank(): Ranks our data by columns (so, at this point, the column for our independent
			variable would look like 1,2,3,...,n).

		* [dependent]: After ranking, take the column represented by our dependent variable.

		* values: Switches from the pandas dataframe representation to the numpy array representation
			(necessary for ediff1d).

		* np.ediff1d: Takes the successive differences of the numbers representing the ranks of the
			dependent variable with respect to the independent variable.
			For example: 
				In [3]: arr = array([1,3,2,5,4])

				In [4]: np.ediff1d(arr)
				Out[4]: array([ 2, -1,  3, -1])

		* np.vectorize(abs): Takes the absolute value of each element in the array of deltas produced
			by np.ediff1d.

		* mean(): Finally, take the mean of the absolute values provided in the previous step.

		"""

		return np.vectorize(abs)(np.ediff1d(self.dataFrame.sort([independent]).rank()[dependent].values)).mean()

	def computeUCC(self):

		n = self.dataFrame.shape[0]
		m = len(self.columns)

		results = []

		for i in list(range(m-1)):
			for j in list(range(i+1,m)):
				independent = self.columns[i]
				dependent = self.columns[j]

				ucc_y = 1 - ( self.__avg_of_abs_deltas(independent,dependent) * 3 ) / (n + 1)
				ucc_x = 1 - ( self.__avg_of_abs_deltas(dependent,independent) * 3 ) / (n + 1)

				ucc = max([ucc_x,ucc_y])

				row = [independent,dependent,ucc_x,ucc_y,ucc]

				results.append(row)

		return DataFrame(results,columns=['col1','col2','ucc_x','ucc_y','ucc'])
