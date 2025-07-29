from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol, validate_quantity, validate_price
from src.logger import log_info, log_error

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        stop_price = validate_price(stop_price)
        limit_price = validate_price(limit_price)
        side = side.upper()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity,
            price=limit_price,
            timeInForce="GTC"
        )

        log_info(f"Stop-Limit order placed: {order}")
        print("✅ Stop-Limit Order Executed.")
    except Exception as e:
        log_error(f"Stop-Limit error: {e}")
        print(f"❌ Error: {e}")
