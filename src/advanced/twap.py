import time
from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_twap_order(symbol, side, total_quantity, slices=5, interval_sec=10):
    slice_qty = total_quantity / slices
    results = []

    for i in range(slices):
        payload = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": round(slice_qty, 6),
            "timestamp": client._get_timestamp(),
            "recvWindow": 10000
        }

        logger.info(f"TWAP: Placing slice {i+1}/{slices}")
        result = client.place_order(payload)
        results.append(result)
        time.sleep(interval_sec)

    logger.info("TWAP Order Complete")
    return results
