"""
cli.py


Command-line interface for the trading bot. Parses args, loads credentials, and routes to BasicBot and order_types.
"""
import argparse
import os
import logging
import sys
from typing import Any


from .basic_bot import BasicBot
from .order_types import TWAP, StopLimitCombo


# configure root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("sample_logs/basic_bot.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s
