# import sys
# from src.binance_client import BinanceFuturesREST
# from validators import validate_symbol, validate_side, validate_positive_float

# def place_stop_limit_order(symbol, side, quantity, price, stop_price):
#     if not all([
#         validate_symbol(symbol),
#         validate_side(side),
#         validate_positive_float(quantity),
#         validate_positive_float(price),
#         validate_positive_float(stop_price)
#     ]):
#         return {"error": "Invalid input"}

#     client = BinanceFuturesREST()
#     data = {
#         "symbol": symbol.upper(),
#         "side": side.upper(),
#         "type": "STOP",
#         "timeInForce": "GTC",
#         "quantity": quantity,
#         "price": price,
#         "stopPrice": stop_price
#     }
#     return client.place_order(data)

# if __name__ == "__main__":
#     if len(sys.argv) != 6:
#         print("Usage: python src/advanced/stop_limit.py SYMBOL BUY/SELL QUANTITY PRICE STOP_PRICE")
#     else:
#         _, symbol, side, quantity, price, stop_price = sys.argv
#         result = place_stop_limit_order(symbol, side, quantity, price, stop_price)
#         print(result)

from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": "STOP",
        "quantity": quantity,
        "price": limit_price,
        "stopPrice": stop_price,
        "timeInForce": "GTC",
        "timestamp": client._get_timestamp(),
        "recvWindow": 10000
    }

    return client.place_order(payload)
