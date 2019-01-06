# coding: utf-8

"""
    BlockMarkets Cryptocurrency API

    The BlockMarkets API provides real-time and historical market data on cryptocurrencies from the world's leading crypto exchanges. Sign up for a free, unlimited API key at [BlockMarkets Cryptocurrency API](https://www.blockmarkets.io/cryptocurrency-api).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "blockmarkets"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="BlockMarkets API Python SDK",
    author="BlockMarkets, Inc."
    author_email="",
    url="https://github.com/BlockMarkets/python-rest-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "BlockMarkets Cryptocurrency API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The BlockMarkets API provides real-time and historical market data on cryptocurrencies from the world&#39;s leading crypto exchanges. Sign up for a free, unlimited API key at [BlockMarkets Cryptocurrency API](https://www.blockmarkets.io/cryptocurrency-api).  # noqa: E501
    """
)