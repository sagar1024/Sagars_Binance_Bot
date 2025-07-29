import sys
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import place_twap_orders
from src.advanced.grid import place_grid_orders
from src.logger import log_error

def print_usage():
    print("""
          
    Sagar Gurung's Binance Bot CLI

    Choose an option:
    1. Market Order
    2. Limit Order
    3. Stop-Limit Order
    4. OCO Order (Spot Only)
    5. TWAP Strategy
    6. Grid Strategy

    """)

def main():
    print_usage()
    choice = input("Enter your choice (1-6): ").strip()

    try:
        if choice == "1":
            symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
            side = input("BUY or SELL: ").strip().upper()
            quantity = input("Quantity: ").strip()
            place_market_order(symbol, side, quantity)

        elif choice == "2":
            symbol = input("Enter symbol: ").strip().upper()
            side = input("BUY or SELL: ").strip().upper()
            quantity = input("Quantity: ").strip()
            price = input("Limit Price: ").strip()
            place_limit_order(symbol, side, quantity, price)

        elif choice == "3":
            symbol = input("Enter symbol: ").strip().upper()
            side = input("BUY or SELL: ").strip().upper()
            quantity = input("Quantity: ").strip()
            price = input("Limit Price: ").strip()
            stop_price = input("Stop Price: ").strip()
            place_stop_limit_order(symbol, side, quantity, price, stop_price)

        elif choice == "4":
            symbol = input("Enter symbol (SPOT MARKET ONLY): ").strip().upper()
            quantity = input("Quantity: ").strip()
            price = input("Limit Price: ").strip()
            stop_price = input("Stop Price: ").strip()
            stop_limit_price = input("Stop-Limit Price: ").strip()
            place_oco_order(symbol, quantity, price, stop_price, stop_limit_price)

        elif choice == "5":
            symbol = input("Enter symbol: ").strip().upper()
            side = input("BUY or SELL: ").strip().upper()
            quantity = input("Total Quantity: ").strip()
            chunks = input("Number of Chunks: ").strip()
            interval = input("Interval between chunks (seconds): ").strip()
            place_twap_orders(symbol, side, quantity, int(chunks), int(interval))

        elif choice == "6":
            symbol = input("Enter symbol: ").strip().upper()
            side = input("BUY or SELL: ").strip().upper()
            lower_price = input("Lower Price: ").strip()
            upper_price = input("Upper Price: ").strip()
            grid_count = input("Number of grid levels: ").strip()
            qty_per_order = input("Quantity per order: ").strip()
            place_grid_orders(symbol, side, lower_price, upper_price, int(grid_count), qty_per_order)

        else:
            print("Invalid choice.")
            print_usage()

    except Exception as e:
        log_error(f"Exception occurred in CLI: {e}")
        print("Something went wrong. Please check logs or retry.")

if __name__ == "__main__":
    main()
