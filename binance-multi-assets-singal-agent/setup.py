# setup.py
from setuptools import setup, find_packages

setup(
    name="binance_trading_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pandas_ta',
        'matplotlib',
        'python-binance'
    ],
    entry_points={
        'console_scripts': [
            'binance_trading_bot = binance_trading_bot.__main__:main'
        ]
    }
)
