import setuptools
import os

from mypower.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypower", # Replace with your own username
    version=__version__,
    author="Muhammad Yasirroni",
    author_email="muhammadyasirroni@gmail.com",
    description="Supplementary function and Python port of MATPOWER",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasirroni/mypower",
    packages=setuptools.find_packages(),
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Scientific Engineering :: Mathematics",
    ],
    python_requires='>=3.6',
    install_requires = [
        "numpy",
        "oct2py"
    ]
)
