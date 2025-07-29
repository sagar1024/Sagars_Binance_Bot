from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol
from src.logger import log_info, log_error

def execute_grid_strategy(symbol, side, lower_price, upper_price, grid_count, quantity):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        side = side.upper()
        step = (upper_price - lower_price) / (grid_count - 1)

        for i in range(grid_count):
            price = round(lower_price + i * step, 2)

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                price=price,
                quantity=quantity,
                timeInForce="GTC"
            )

            log_info(f"Grid order {i+1}: {order}")
            print(f"✅ Grid order {i+1}/{grid_count} placed at {price}")
    except Exception as e:
        log_error(f"Grid error: {e}")
        print(f"❌ Error: {e}")
