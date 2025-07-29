from binance.client import Client
from src.config import API_KEY, API_SECRET, BASE_URL
from src.logger import log_info, log_error

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL

def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            stopPrice=str(stop_price),
            quantity=str(quantity),
            price=str(price),
            timeInForce="GTC"
        )
        log_info(f"Stop-Limit Order placed: {order}")
        return order
    except Exception as e:
        log_error(f"Failed to place Stop-Limit Order: {e}")
        return None
