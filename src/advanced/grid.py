from src.config import get_binance_client
from src.logger import log_info, log_error
from src.utils import validate_symbol, validate_price, validate_quantity

def place_grid_orders(symbol, side, lower_price, upper_price, grid_count, quantity_per_order):
    client = get_binance_client()

    if not all([
        validate_symbol(client, symbol),
        validate_price(lower_price),
        validate_price(upper_price),
        validate_quantity(quantity_per_order),
    ]):
        log_error("Invalid input for Grid strategy.")
        return

    try:
        lower = float(lower_price)
        upper = float(upper_price)
        step = (upper - lower) / (int(grid_count) - 1)
        quantity = float(quantity_per_order)

        for i in range(int(grid_count)):
            price = round(lower + i * step, 2)
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            log_info(f"[Grid] Limit order placed at {price}: {order}")
    except Exception as e:
        log_error(f"Failed to place grid orders: {e}")
