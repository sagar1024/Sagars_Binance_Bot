from src.config import get_binance_client
from src.logger import log_info, log_error
from src.utils import validate_symbol, validate_quantity, validate_price

def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    client = get_binance_client()

    if not all([
        validate_symbol(client, symbol),
        validate_quantity(quantity),
        validate_price(price),
        validate_price(stop_price)
    ]):
        log_error("Invalid input detected. Order aborted.")
        return

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            quantity=quantity,
            stopPrice=stop_price,
            price=price,
            timeInForce="GTC"
        )
        log_info(f"Stop-limit order placed: {order}")
    except Exception as e:
        log_error(f"Failed to place stop-limit order: {e}")
