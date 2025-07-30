# import sys
# from src.binance_client import BinanceFuturesREST
# from validators import validate_symbol, validate_side, validate_positive_float

# def place_limit_order(symbol, side, quantity, price):
#     if not all([
#         validate_symbol(symbol),
#         validate_side(side),
#         validate_positive_float(quantity),
#         validate_positive_float(price)
#     ]):
#         return {"error": "Invalid input"}

#     client = BinanceFuturesREST()
#     data = {
#         "symbol": symbol.upper(),
#         "side": side.upper(),
#         "type": "LIMIT",
#         "timeInForce": "GTC",
#         "quantity": quantity,
#         "price": price
#     }
#     return client.place_order(data)

# if __name__ == "__main__":
#     if len(sys.argv) != 5:
#         print("Usage: python src/limit_orders.py SYMBOL BUY/SELL QUANTITY PRICE")
#     else:
#         _, symbol, side, quantity, price = sys.argv
#         result = place_limit_order(symbol, side, quantity, price)
#         print(result)

from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_limit_order(symbol, side, quantity, price):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC",
        "timestamp": client._get_timestamp(),
        "recvWindow": 10000
    }
    return client.place_order(payload)
