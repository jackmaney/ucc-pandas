ucc-pandas
==========

An implementation of the Universal Correlation Coefficient in Python via Pandas

[Here](http://www.jackmaney.com/code/universal_correlation_coefficient) is a high-level overview, based on the [R library](https://github.com/jackmaney/ucc) that I wrote to compute the UCC. In a nutshell, for two discrete random variables, the UCC gives an indication as to whether or not there is a--possibly non-linear--relationship between them.

TODO
==========

* Include tests and examples
* ~~Extend to computing UCCs for pairs of columns from a given list~~
    * Also, allow for automatic output of scatterplots for pairs having UCC >= a given threshold
* Print modes:
    * Pretty print mode (for interactive use)
    * CSV output mode (for dumping to file for later).
* Figure out how to make a proper pip package out of this (with `setup.py` and all that happy stuff).
