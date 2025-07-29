from src.config import get_binance_client
from src.logger import log_info, log_error
from src.utils import validate_symbol, validate_quantity

def place_market_order(symbol, side, quantity):
    client = get_binance_client()

    if not validate_symbol(client, symbol):
        log_error(f"Invalid symbol: {symbol}")
        return

    if not validate_quantity(quantity):
        log_error(f"Invalid quantity: {quantity}")
        return

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        log_info(f"Market order placed: {response}")
    except Exception as e:
        log_error(f"Failed to place market order: {e}")
