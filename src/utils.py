from binance.exceptions import BinanceAPIException
from src.logger import log_error

# def validate_symbol(client, symbol):
#     try:
#         info = client.futures_exchange_info()
#         symbols = [s["symbol"] for s in info["symbols"]]
#         return symbol in symbols
#     except BinanceAPIException as e:
#         log_error(f"Error fetching exchange info: {e}")
#         return False

def validate_symbol(client, symbol, spot=False):
    try:
        if spot:
            exchange_info = client.get_exchange_info()
        else:
            exchange_info = client.futures_exchange_info()
        symbols = [s['symbol'] for s in exchange_info['symbols']]
        return symbol.upper() in symbols
    except Exception as e:
        log_error(f"Symbol validation failed: {e}")
        return False


def validate_quantity(quantity):
    try:
        q = float(quantity)
        return q > 0
    except ValueError:
        return False

def validate_price(price):
    try:
        p = float(price)
        return p > 0
    except ValueError:
        return False
