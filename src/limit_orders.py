from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol, validate_quantity, validate_price
from src.logger import log_info, log_error

def place_limit_order(symbol, side, quantity, price):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        price = validate_price(price)
        side = side.upper()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        log_info(f"Limit order placed: {order}")
        print("✅ Limit Order Executed.")
    except Exception as e:
        log_error(f"Limit order error: {e}")
        print(f"❌ Error: {e}")
