"""
except Exception:
return {"error": str(e)}


# Market order
def place_market_order(self, symbol: str, side: str, quantity: float, reduce_only: bool = False) -> Dict[str, Any]:
if side.upper() not in ("BUY", "SELL"):
raise ValueError("side must be BUY or SELL")
params = {
"symbol": symbol.upper(),
"side": side.upper(),
"type": "MARKET",
"quantity": float(quantity),
"reduceOnly": str(reduce_only).lower(),
}
logger.info("Placing MARKET %s %s %s", side.upper(), symbol.upper(), quantity)
return self._request_signed("POST", ORDER_PATH, params)


# Limit order
def place_limit_order(self, symbol: str, side: str, quantity: float, price: float, time_in_force: str = "GTC", reduce_only: bool = False) -> Dict[str, Any]:
tif = time_in_force.upper()
if tif not in ("GTC", "IOC", "FOK"):
raise ValueError("timeInForce must be one of GTC, IOC, FOK")
params = {
"symbol": symbol.upper(),
"side": side.upper(),
"type": "LIMIT",
"quantity": float(quantity),
"price": str(price),
"timeInForce": tif,
"reduceOnly": str(reduce_only).lower(),
}
logger.info("Placing LIMIT %s %s %s @ %s", side.upper(), symbol.upper(), quantity, price)
return self._request_signed("POST", ORDER_PATH, params)


# Stop Market order (triggered market order). Futures supports STOP_MARKET type via API.
def place_stop_market(self, symbol: str, side: str, quantity: float, stop_price: float, close_position: bool = False) -> Dict[str, Any]:
# closePosition True will attempt to close the position instead of specifying quantity.
params = {
"symbol": symbol.upper(),
"side": side.upper(),
"type": "STOP_MARKET",
"stopPrice": str(stop_price),
"closePosition": str(close_position).lower(),
}
if not close_position:
params["quantity"] = float(quantity)
logger.info("Placing STOP_MARKET %s %s qty=%s stop=%s", side.upper(), symbol.upper(), quantity, stop_price)
return self._request_signed("POST", ORDER_PATH, params)


# Simple helper to validate returned order
@staticmethod
def summarize_response(resp: Dict[str, Any]) -> str:
if resp is None:
return "No response"
if "error" in resp:
return f"ERROR: {resp['error']}"
# Typical fields: symbol, orderId, status, executedQty, origQty, price
return f"symbol={resp.get('symbol')} id={resp.get('orderId')} status={resp.get('status')} executed={resp.get('executedQty')} orig={resp.get('origQty')}"
