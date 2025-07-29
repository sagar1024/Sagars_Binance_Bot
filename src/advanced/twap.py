import time
from src.market_orders import place_market_order
from src.logger import log_info

def place_twap_order(symbol, side, quantity, intervals, delay):
    quantity = float(quantity)
    slice_qty = quantity / intervals

    log_info(f"Placing TWAP order: {intervals} intervals of {slice_qty} every {delay}s")

    for i in range(intervals):
        log_info(f"Placing TWAP slice {i+1}/{intervals}")
        place_market_order(symbol, side, slice_qty)
        time.sleep(delay)
