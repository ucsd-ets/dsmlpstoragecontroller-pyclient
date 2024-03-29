import codecs
import os.path
from sys import version_info

from setuptools import find_packages, setup

MIN_PYTHON_VERSION = f"{version_info.major}.{version_info.minor}.0"


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as readme_file:
        long_description = readme_file.read()
    return long_description


setup(
    name="dsmlpstoragecontrollerclient",
    version=get_version("src/dsmlpstoragecontrollerclient/__init__.py"),
    author="Naval Patel",
    author_email="nhp002@ucsd.edu",
    description="Python client of the DSMLP Storage Controller gRPC Service",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient",
    project_urls={
        "Bug Tracker": "https://github.com/ucsd-ets/dsmlpstoragecontroller-pyclient/issues",
    },
    classifiers=[
        f"Programming Language :: Python :: {MIN_PYTHON_VERSION}",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=f">={MIN_PYTHON_VERSION}",
    install_requires=["grpcio>=1.46.3", "grpcio-tools>=1.46.3"],
)
