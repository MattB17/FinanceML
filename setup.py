from setuptools import setup, find_packages
from os import path
from io import open

# Get current directory and long description from README
current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, "README.md")) as f:
    longDescription = f.read()

# the setup
setup(
    name="FinanceML",
    version="0.1.0",
    description="Machine Learning for Finance",
    long_description=longDescription,
    authors="Amogh Reddy, Matt Buckley",
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
