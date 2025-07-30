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
