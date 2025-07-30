# import sys
# import requests
# from src.binance_client import BinanceFuturesREST
# from config import BASE_URL
# from validators import validate_symbol, validate_positive_float

# def get_current_price(symbol):
#     url = f"{BASE_URL}/fapi/v1/ticker/price?symbol={symbol.upper()}"
#     return float(requests.get(url).json()["price"])

# def place_grid_orders(symbol, quantity, grid_size=3, interval=50):
#     if not all([
#         validate_symbol(symbol),
#         validate_positive_float(quantity)
#     ]):
#         return {"error": "Invalid input"}

#     client = BinanceFuturesREST()
#     current_price = get_current_price(symbol)
#     responses = []

#     for i in range(1, grid_size + 1):
#         buy_price = round(current_price - i * interval, 2)
#         sell_price = round(current_price + i * interval, 2)

#         # Buy Order
#         buy_order = {
#             "symbol": symbol.upper(),
#             "side": "BUY",
#             "type": "LIMIT",
#             "timeInForce": "GTC",
#             "quantity": quantity,
#             "price": buy_price
#         }

#         # Sell Order
#         sell_order = {
#             "symbol": symbol.upper(),
#             "side": "SELL",
#             "type": "LIMIT",
#             "timeInForce": "GTC",
#             "quantity": quantity,
#             "price": sell_price
#         }

#         responses.append(client.place_order(buy_order))
#         responses.append(client.place_order(sell_order))

#     return responses

# if __name__ == "__main__":
#     if len(sys.argv) != 4:
#         print("Usage: python src/advanced/grid.py SYMBOL QUANTITY GRID_SIZE")
#     else:
#         _, symbol, quantity, grid_size = sys.argv
#         result = place_grid_orders(symbol, float(quantity), int(grid_size))
#         print(result)

from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_grid_orders(symbol, base_price, grid_size, price_step, quantity):
    results = []

    for i in range(1, grid_size + 1):
        buy_price = round(base_price - (price_step * i), 2)
        sell_price = round(base_price + (price_step * i), 2)

        buy_payload = {
            "symbol": symbol,
            "side": "BUY",
            "type": "LIMIT",
            "quantity": quantity,
            "price": buy_price,
            "timeInForce": "GTC",
            "timestamp": client._get_timestamp(),
            "recvWindow": 10000
        }

        sell_payload = {
            "symbol": symbol,
            "side": "SELL",
            "type": "LIMIT",
            "quantity": quantity,
            "price": sell_price,
            "timeInForce": "GTC",
            "timestamp": client._get_timestamp(),
            "recvWindow": 10000
        }

        logger.info(f"Grid: Placing BUY at {buy_price}, SELL at {sell_price}")
        results.append(client.place_order(buy_payload))
        results.append(client.place_order(sell_payload))

    logger.info("Grid Orders Complete")
    return results
