from src.config import get_binance_client
from src.logger import log_info, log_error
from src.utils import validate_symbol, validate_quantity, validate_price

def place_limit_order(symbol, side, quantity, price):
    client = get_binance_client()

    if not validate_symbol(client, symbol):
        log_error(f"Invalid symbol: {symbol}")
        return

    if not validate_quantity(quantity):
        log_error(f"Invalid quantity: {quantity}")
        return

    if not validate_price(price):
        log_error(f"Invalid price: {price}")
        return

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        log_info(f"Limit order placed: {response}")
    except Exception as e:
        log_error(f"Failed to place limit order: {e}")
