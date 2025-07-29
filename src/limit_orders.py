from binance.client import Client
from src.config import API_KEY, API_SECRET, BASE_URL
from src.logger import log_info, log_error

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        log_info(f"Limit Order placed: {order}")
        return order
    except Exception as e:
        log_error(f"Failed to place Limit Order: {e}")
        return None
