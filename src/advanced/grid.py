from src.limit_orders import place_limit_order
from src.logger import log_info

def place_grid_orders(symbol, side, quantity, start_price, price_interval, num_orders):
    log_info(f"Placing Grid Strategy: {num_orders} orders from {start_price} with interval {price_interval}")

    start_price = float(start_price)
    price_interval = float(price_interval)

    for i in range(num_orders):
        price = start_price + (i * price_interval)
        log_info(f"Placing limit order at {price}")
        place_limit_order(symbol, side, quantity, price)
