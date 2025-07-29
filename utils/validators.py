from binance.client import Client
from src.config import API_KEY, API_SECRET, BASE_URL
from src.logger import log_error

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL

# def is_valid_symbol(symbol):
#     try:
#         exchange_info = client.futures_exchange_info()
#         symbols = [s["symbol"] for s in exchange_info["symbols"]]
#         return symbol.upper() in symbols
#     except Exception as e:
#         log_error(f"Symbol validation failed: {e}")
#         return False

def is_valid_symbol(symbol):
    try:
        exchange_info = client.futures_exchange_info()
        symbols = [s["symbol"] for s in exchange_info.get("symbols", [])]
        return symbol.upper() in symbols
    except Exception as e:
        if hasattr(e, 'message'):
            log_error(f"Symbol validation failed: {e.message}")
        else:
            log_error(f"Symbol validation failed: {e}")
        return False

def is_valid_side(side):
    return side.upper() in ["BUY", "SELL"]

def is_positive_float(value):
    try:
        val = float(value)
        return val > 0
    except ValueError:
        return False
