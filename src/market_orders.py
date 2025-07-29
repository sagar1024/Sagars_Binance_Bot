from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol, validate_quantity
from src.logger import log_info, log_error

def place_market_order(symbol, side, quantity):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        side = side.upper()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        log_info(f"Market order placed: {order}")
        print("✅ Market Order Executed.")
    except Exception as e:
        log_error(f"Market order error: {e}")
        print(f"❌ Error: {e}")
