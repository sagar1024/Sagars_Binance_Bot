from binance.client import Client
from src.config import API_KEY, API_SECRET, BASE_URL
from src.logger import log_info, log_error

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        log_info(f"Market Order placed: {order}")
        return order
    except Exception as e:
        log_error(f"Failed to place Market Order: {e}")
        return None
