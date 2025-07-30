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
