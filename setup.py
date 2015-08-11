import setuptools
from ucc_pandas import __version__

setuptools.setup(
    name='ucc-pandas',
    version=__version__,
    url='https://github.com/jackmaney/ucc-pandas',
    license='MIT',
    author='Jack Maney',
    author_email='jackmaney@gmail.com',
    description='An implementation of the Universal Correlation Coefficient in Python via Pandas',
    install_requires=["pandas",
                      "numpy"],
    packages=setuptools.find_packages(exclude="examples")
)
