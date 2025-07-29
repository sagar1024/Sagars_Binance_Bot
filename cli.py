from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import execute_twap
from src.advanced.grid import execute_grid_strategy

def main():
    while True:
        print("\nChoose an Order Type:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Stop-Limit Order")
        print("4. OCO Order")
        print("5. TWAP Strategy")
        print("6. Grid Strategy")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        try:
            if choice == "1":
                symbol = input("Symbol: ")
                side = input("Side (BUY/SELL): ")
                qty = input("Quantity: ")
                place_market_order(symbol, side, qty)

            elif choice == "2":
                symbol = input("Symbol: ")
                side = input("Side (BUY/SELL): ")
                qty = input("Quantity: ")
                price = input("Price: ")
                place_limit_order(symbol, side, qty, price)

            elif choice == "3":
                symbol = input("Symbol: ")
                side = input("Side (BUY/SELL): ")
                qty = input("Quantity: ")
                stop_price = input("Stop Price: ")
                limit_price = input("Limit Price: ")
                place_stop_limit_order(symbol, side, qty, stop_price, limit_price)

            elif choice == "4":
                symbol = input("Symbol: ")
                qty = input("Quantity: ")
                tp = input("Take-Profit Price: ")
                sl = input("Stop-Loss Price: ")
                place_oco_order(symbol, qty, tp, sl)

            elif choice == "5":
                symbol = input("Symbol: ")
                side = input("Side (BUY/SELL): ")
                total_qty = input("Total Quantity: ")
                chunks = int(input("Chunks: "))
                interval = int(input("Interval (seconds): "))
                execute_twap(symbol, side, total_qty, chunks, interval)

            elif choice == "6":
                symbol = input("Symbol: ")
                side = input("Side (BUY/SELL): ")
                low = float(input("Lower Price: "))
                high = float(input("Upper Price: "))
                grids = int(input("Grid Count: "))
                qty = float(input("Qty per Order: "))
                execute_grid_strategy(symbol, side, low, high, grids, qty)

            elif choice == "0":
                print("Exiting.")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
