# import sys
# import time
# from src.binance_client import BinanceFuturesREST
# from validators import validate_symbol, validate_side, validate_positive_float

# def place_twap_order(symbol, side, total_quantity, chunks=5, interval_sec=2):
#     if not all([
#         validate_symbol(symbol),
#         validate_side(side),
#         validate_positive_float(total_quantity)
#     ]):
#         return {"error": "Invalid input"}

#     chunk_size = round(float(total_quantity) / chunks, 6)
#     client = BinanceFuturesREST()
#     responses = []

#     for i in range(chunks):
#         data = {
#             "symbol": symbol.upper(),
#             "side": side.upper(),
#             "type": "MARKET",
#             "quantity": chunk_size
#         }
#         response = client.place_order(data)
#         responses.append(response)
#         time.sleep(interval_sec)

#     return responses

# if __name__ == "__main__":
#     if len(sys.argv) != 5:
#         print("Usage: python src/advanced/twap.py SYMBOL BUY/SELL TOTAL_QUANTITY CHUNKS")
#     else:
#         _, symbol, side, total_quantity, chunks = sys.argv
#         result = place_twap_order(symbol, side, total_quantity, int(chunks))
#         print(result)

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
