import setuptools
from ucc_pandas import __version__

try:
    with open("requirements.txt") as f:
        requirements = [x for x in f.read().splitlines() if x.strip()]
except IOError as e:
    requirements = []

setuptools.setup(
    name='ucc-pandas',
    version=__version__,
    url='https://github.com/jackmaney/ucc-pandas',
    license='MIT',
    author='Jack Maney',
    author_email='jackmaney@gmail.com',
    description='An implementation of the Universal Correlation Coefficient in Python via Pandas',
    install_requires=requirements,
    packages=setuptools.find_packages(exclude="examples"),
    entry_points={
        "console_scripts": [
            "ucc=ucc_pandas:main"
        ]
    }
)
