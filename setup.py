import setuptools
import os

from mypower.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

def package_files(directory_list):
    paths = []
    for directory in directory_list:
        for (path, _, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files([
    'mypower/matpower/data',
    'mypower/matpower/docker',
    'mypower/matpower/docs',
    'mypower/matpower/lib',
    'mypower/matpower/mips',
    'mypower/matpower/most',
    'mypower/matpower/mp-opt-model',
    'mypower/matpower/mptest'
    ])

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
    package_data={
        '': extra_files,
        'mypower':[
            'matpower/AUTHORS',
            'matpower/CHANGES.md',
            'matpower/CITATION',
            'matpower/CONTRIBUTING.md',
            'matpower/install_matpower.m',
            'matpower/LICENSE',
            'matpower/README.md'
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Scientific Engineering :: Mathematics",
    ],
    python_requires='>=3.6',
)
