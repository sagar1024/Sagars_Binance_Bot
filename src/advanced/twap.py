import time
from src.config import get_binance_client
from src.logger import log_info, log_error
from src.utils import validate_symbol, validate_quantity

def place_twap_orders(symbol, side, quantity, chunks, interval_seconds):
    client = get_binance_client()

    if not validate_symbol(client, symbol):
        log_error(f"Invalid symbol: {symbol}")
        return

    try:
        chunk_quantity = round(float(quantity) / int(chunks), 6)
        for i in range(int(chunks)):
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=chunk_quantity
            )
            log_info(f"[TWAP] Order {i+1}/{chunks} placed: {order}")
            if i < chunks - 1:
                time.sleep(int(interval_seconds))
    except Exception as e:
        log_error(f"Failed during TWAP execution: {e}")
