import time
from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol, validate_quantity
from src.logger import log_info, log_error

def execute_twap(symbol, side, total_quantity, chunks, interval_seconds):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        side = side.upper()
        total_quantity = validate_quantity(total_quantity)
        qty_per_order = round(total_quantity / chunks, 6)

        for i in range(chunks):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty_per_order
            )
            log_info(f"TWAP order chunk {i+1}: {order}")
            print(f"✅ Chunk {i+1}/{chunks} placed.")
            time.sleep(interval_seconds)
    except Exception as e:
        log_error(f"TWAP error: {e}")
        print(f"❌ Error: {e}")
