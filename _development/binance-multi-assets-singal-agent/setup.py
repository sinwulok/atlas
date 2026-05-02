# setup.py
from setuptools import setup, find_packages

setup(
    name="binance_trading_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pandas-ta',
        'numpy<2',
        'python-binance',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'binance_trading_bot = src.app.main:main'
        ]
    }
)
