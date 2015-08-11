from pandas import DataFrame
import numpy as np

__all__ = ["UCC"]


class UCC(object):
    def __init__(self, data_frame, columns=None,
                 x=None, y=None, clone=False):

        UCC._validate_input(data_frame)

        if clone:
            self.data_frame = data_frame.copy()
        else:
            self.data_frame = data_frame

        if x is not None and y is not None:
            self.columns = [x, y]
        elif columns is not None:
            self.columns = columns
        else:
            self.columns = data_frame.columns

        self._check_columns()

        self.data_frame = self.data_frame.drop_duplicates(columns)

    @staticmethod
    def _validate_input(data_frame):

        if not isinstance(data_frame, DataFrame):
            raise Exception("data_frame argument is not a pandas DataFrame")
        elif data_frame.empty:
            raise Exception("The given data frame is empty")
        elif data_frame.shape[1] < 2:
            raise Exception("The given data frame must have at least two columns")

    def _check_columns(self):
        if len(self.columns) < 2:
            raise Exception("At least two columns are required")

        for col in self.columns:
            if col not in self.data_frame.columns:
                raise Exception("There is no column in the given data frame by the name of '%s'" % col)
            if not self.__is_numeric(col):
                raise Exception("The column '%s' is either not numeric or contains NaN values" % col)

    def __is_numeric(self, col):
        return all(np.isreal(self.data_frame[col])) and not any(np.isnan(self.data_frame[col]))

    def __avg_of_abs_deltas(self, independent, dependent):
        """
        This could be done in a way that's more easy to read, but I wanted to use the built-in functionality in pandas and numpy. So, unwrapping this from the inside out:

        * self.data_frame.sort([independent]): sorts our data by the column name for the independent variable.

        * .rank(): Ranks our data by columns (so, at this point, the column for our independent variable would look like 1,2,3,...,n).

        * [dependent]: After ranking, take the column represented by our dependent variable.

        * values: Switches from the pandas dataframe representation to the numpy array representation (necessary for ediff1d).

        * np.ediff1d: Takes the successive differences of the numbers representing the ranks of the dependent variable with respect to the independent variable. For example:

::

    In [3]: arr = array([1,3,2,5,4])
    In [4]: np.ediff1d(arr)
    Out[4]: array([ 2, -1,  3, -1])

    * np.vectorize(abs): Takes the absolute value of each element in the array of deltas produced by np.ediff1d.

    * mean(): Finally, take the mean of the absolute values provided in the previous step."""

        return np.vectorize(abs)(np.ediff1d(self.data_frame.sort([independent]).rank()[dependent].values)).mean()

    def compute_ucc(self):

        n = self.data_frame.shape[0]
        m = len(self.columns)

        results = []

        for i in range(m - 1):
            for j in range(i + 1, m):
                independent = self.columns[i]
                dependent = self.columns[j]

                avg_y = self.__avg_of_abs_deltas(independent, dependent)
                avg_x = self.__avg_of_abs_deltas(dependent, independent)

                ucc_y = 1 - (avg_y * 3.0) / (n + 1)
                ucc_x = 1 - (avg_x * 3.0) / (n + 1)

                ucc = max([ucc_x, ucc_y])

                row = [independent, dependent, ucc_x, ucc_y, ucc]

                results.append(row)

        return DataFrame(results,
                         columns=['col1', 'col2', 'ucc_x', 'ucc_y', 'ucc'])
