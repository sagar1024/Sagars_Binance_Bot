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
