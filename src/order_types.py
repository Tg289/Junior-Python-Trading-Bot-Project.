"""
order_types.py
Higher-level order flows built on BasicBot: TWAP implementation and helpers for stop/limit combos.
"""
import time
import logging
from typing import List, Dict, Any
from .basic_bot import BasicBot
logger = logging.getLogger("order_types")


class TWAP:
def __init__(self, bot: BasicBot):
self.bot = bot


def run(self, symbol: str, side: str, total_quantity: float, parts: int = 4, interval: int = 10) -> List[Dict[str, Any]]:
if parts < 1:
raise ValueError("parts must be >= 1")
per_part = float(total_quantity) / parts
results = []
logger.info("TWAP start: %s %s total=%s parts=%d interval=%ds", side.upper(), symbol.upper(), total_quantity, parts, interval)
for i in range(parts):
logger.info("TWAP part %d/%d: placing market order for %s", i + 1, parts, per_part)
res = self.bot.place_market_order(symbol, side, per_part)
results.append(res)
if i < parts - 1:
time.sleep(interval)
logger.info("TWAP complete")
return results




class StopLimitCombo:
"""Simple helper that places a limit order and a stop-market trigger for risk management.
Note: Futures platforms differ; this helper demonstrates an approach but ensure symbol params and exchange rules are followed.
"""


def __init__(self, bot: BasicBot):
self.bot = bot


def place(self, symbol: str, side: str, quantity: float, limit_price: float, stop_price: float) -> List[Dict[str, Any]]:
results = []
# Place limit order
limit_res = self.bot.place_limit_order(symbol, side, quantity, limit_price)
results.append({"limit": limit_res})
# Place stop market to protect
# Stop side should be opposite of entry side for protective stop
stop_side = "SELL" if side.upper() == "BUY" else "BUY"
stop_res = self.bot.place_stop_market(symbol, stop_side, quantity, stop_price, close_position=False)
results.append({"stop": stop_res})
return results
