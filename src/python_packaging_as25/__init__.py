"""Test for Python packaging."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("python-packaging-AS25")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "André Scholl"
__email__ = "andre.scholl@unibe.ch"
