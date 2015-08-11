from . import __version__
import click
import pandas as pd
import csv
import sys

from .base import UCC


@click.command()
@click.version_option(version=__version__)
@click.argument("input_file", type=click.File("r"))
@click.argument("output_file", type=click.File("w"))
@click.option("--header/--no-header", default=True,
              help="Does the input have a header? (defaults to 'yes')")
@click.option("--columns", default=None,
              help="A comma-delimited list of column names or integer positions (0-indexed). Specified columns are the only ones used for computing UCC values. If a list of names is given, the file must have a header, and the given column names must be in the header. If int positions are specified, then only columns in these positions will be used. If this option isn't set, then all columns are used.")
def main(input_file, output_file, header, columns):
    """
    Takes CSV input and outputs UCC data to CSV (use '-' for input/output for STDIN/STDOUT).
    """

    df = pd.read_csv(input_file, header=0 if header else None)

    columns = columns if columns is not None else df.columns

    if not all([col in df.columns for col in columns]):

        raise ValueError("Columns {} not all found in CSV ({})".format(
            ",".join(columns), ",".join(df.columns)
        ))

    ucc = UCC(df, columns=columns, clone=True)

    ucc.compute_ucc(output_type="csv", output_file=output_file)








