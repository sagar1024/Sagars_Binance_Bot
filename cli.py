from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.twap import place_twap_order
from src.advanced.grid import place_grid_orders
from src.advanced.oco import place_oco_order
from utils.validators import is_valid_symbol, is_valid_side, is_positive_float
from src.logger import log_info

def get_input(prompt, validator, error_msg):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print(f"[ERROR] {error_msg}")

def cli():
    print("""
    \033[1mSagar Gurung's Binance Futures Bot CLI\033[0m

    Choose an option:
    1. Market Order
    2. Limit Order
    3. Stop-Limit Order
    4. OCO Order (Not Supported in Futures)
    5. TWAP Strategy
    6. Grid Strategy
    """)

    choice = input("Enter your choice (1-6): ").strip()

    if choice not in {"1", "2", "3", "4", "5", "6"}:
        print("[ERROR] Invalid choice")
        return

    symbol = get_input("Enter symbol (e.g., BTCUSDT): ", is_valid_symbol, "Invalid symbol")
    side = get_input("BUY or SELL: ", is_valid_side, "Invalid side")
    quantity = get_input("Quantity: ", is_positive_float, "Quantity must be a positive number")

    if choice == "1":
        place_market_order(symbol, side.upper(), float(quantity))

    elif choice == "2":
        price = get_input("Limit Price: ", is_positive_float, "Price must be positive")
        place_limit_order(symbol, side.upper(), float(quantity), float(price))

    elif choice == "3":
        stop_price = get_input("Stop Price: ", is_positive_float, "Invalid stop price")
        limit_price = get_input("Limit Price: ", is_positive_float, "Invalid limit price")
        place_stop_limit_order(symbol, side.upper(), float(quantity), float(limit_price), float(stop_price))

    elif choice == "4":
        print("[INFO] OCO orders are not supported on Binance Futures.")
        try:
            place_oco_order()
        except NotImplementedError as e:
            print(f"[ERROR] {e}")

    elif choice == "5":
        intervals = get_input("Number of intervals: ", lambda x: x.isdigit() and int(x) > 0, "Must be a positive integer")
        delay = get_input("Delay between orders (in seconds): ", is_positive_float, "Invalid delay")
        place_twap_order(symbol, side.upper(), float(quantity), int(intervals), float(delay))

    elif choice == "6":
        start_price = get_input("Start Price: ", is_positive_float, "Invalid start price")
        price_interval = get_input("Price Interval: ", is_positive_float, "Invalid interval")
        num_orders = get_input("Number of grid orders: ", lambda x: x.isdigit() and int(x) > 0, "Must be a positive integer")
        place_grid_orders(symbol, side.upper(), float(quantity), float(start_price), float(price_interval), int(num_orders))

if __name__ == "__main__":
    cli()
