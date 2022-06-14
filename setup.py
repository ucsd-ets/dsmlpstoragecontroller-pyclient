from distutils.core import setup
from setuptools import find_packages
import codecs
import os.path


# https://packaging.python.org/guides/single-sourcing-package-version/
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


setup(
    name="dsmlpstoragecontrollerclient",
    version=get_version("dsmlpstoragecontrollerclient/__init__.py"),
    description="Python client of the DSMLP Storage Controller gRPC Service",
    author="Naval Patel",
    author_email="nhp002@ucsd.edu",
    url="",
    packages=find_packages(),
)
