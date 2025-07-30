from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_market_order(symbol, side, quantity):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": client._get_timestamp(),
        "recvWindow": 10000
    }
    return client.place_order(payload)
