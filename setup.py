import setuptools as setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nepal-sub-divisions",
    version="0.0.5",  # Required
    description="Nepali  municipalities is a python package to get data about Nepali municipalities based on districts",
    url="https://github.com/iDineshRoy/nepal-sub-divisions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dinesh Roy",
    author_email="dinesh.roy@hotmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "nepal_municipalities": ["data/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords=[
        "Nepali",
        "nepal",
        "nepal provinces",
        "nepali districts",
        "nepali municipalities",
        "dinesh roy",
        "nepali states",
    ],
)
