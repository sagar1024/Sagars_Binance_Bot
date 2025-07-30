# from binance.client import Client
# from src.config import API_KEY, API_SECRET, BASE_URL
# from src.logger import log_info, log_error
# import requests

# client = Client(API_KEY, API_SECRET)
# client.FUTURES_URL = BASE_URL

# def get_binance_server_time():
#     server_time = requests.get(f"{BASE_URL}/fapi/v1/time").json()["serverTime"]
#     return server_time

# def place_market_order(symbol, side, quantity):
#     try:
#         server_time = get_binance_server_time()
#         if server_time is None:
#             log_error("Could not retrieve server time.")
#             return None

#         order = client.futures_create_order(
#             symbol=symbol,
#             side=side.upper(),
#             type="MARKET",
#             quantity=quantity,
#             timestamp=server_time,
#             recvWindow=10000
#         )
#         log_info(f"Market Order placed: {order}")
#         return order
#     except Exception as e:
#         log_error(f"Failed to place Market Order: {e}")
#         return None

from bot.futures_client import BinanceFuturesREST
from logger import logger

def place_market_order(symbol, side, quantity):
    client = BinanceFuturesREST()
    try:
        return client.place_order(symbol, side, quantity, order_type="MARKET")
    except Exception as e:
        logger.error(f"Failed to place Market Order: {e}")
        return None
