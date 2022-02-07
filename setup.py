import setuptools
import os
import re

PACKAGE_NAME = 'mypower'
current_path = os.path.abspath(os.path.dirname(__file__))
version_line = open(os.path.join(current_path, PACKAGE_NAME, 'version.py'), "rt").read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "mypower", # Replace with your own username
    version = __version__,
    author = "Muhammad Yasirroni",
    author_email = "muhammadyasirroni@gmail.com",
    description = "Supplementary function and Python port of MATPOWER",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/yasirroni/mypower",
    packages = setuptools.find_packages(),
    package_data = {},
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Scientific Engineering :: Mathematics",
    ],
    python_requires = '>=3.6',
    install_requires = [
        "numpy>=1.0.0",
        "oct2py>=5.2."
    ],
    extras_require = {
        "matpower": [
            "matpower>=7.0.0.1"
        ]
    }
)
