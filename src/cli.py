from validators import *
import sys

from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.stop_limit import place_stop_limit_order
from advanced.oco import place_oco_simulated
from advanced.twap import place_twap_order
from advanced.grid import place_grid_orders

def cli_main():
    print("Welcome to Binance Futures Order Bot\n")
    print("Order Types: MARKET, LIMIT, STOP_LIMIT, OCO, TWAP, GRID")
    order_type = input("Enter order type: ").strip().upper()

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT", "OCO", "TWAP", "GRID"]:
        print("Invalid order type.")
        sys.exit(1)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()

    if not (validate_symbol(symbol) and validate_side(side)):
        print("Invalid symbol or side.")
        sys.exit(1)

    #Market Order
    if order_type == "MARKET":
        quantity = input("Enter quantity: ").strip()
        if not validate_positive_float(quantity):
            print("Invalid quantity.")
            sys.exit(1)
        result = place_market_order(symbol, side, float(quantity))

    #Limit Order
    elif order_type == "LIMIT":
        quantity = input("Enter quantity: ").strip()
        price = input("Enter limit price: ").strip()
        if not (validate_positive_float(quantity) and validate_positive_float(price)):
            print("Invalid inputs.")
            sys.exit(1)
        result = place_limit_order(symbol, side, float(quantity), float(price))

    #Stop-Limit Order
    elif order_type == "STOP_LIMIT":
        quantity = input("Enter quantity: ").strip()
        stop_price = input("Enter stop price (trigger): ").strip()
        limit_price = input("Enter limit price: ").strip()
        if not (validate_positive_float(quantity) and validate_positive_float(stop_price) and validate_positive_float(limit_price)):
            print("Invalid inputs.")
            sys.exit(1)
        result = place_stop_limit_order(symbol, side, float(quantity), float(stop_price), float(limit_price))

    #OCO Order (Simulated only)
    elif order_type == "OCO":
        quantity = input("Enter quantity: ").strip()
        take_profit = input("Enter take-profit price: ").strip()
        stop_loss = input("Enter stop-loss price: ").strip()
        if not (validate_positive_float(quantity) and validate_positive_float(take_profit) and validate_positive_float(stop_loss)):
            print("Invalid inputs.")
            sys.exit(1)
        result = place_oco_simulated(symbol, side, float(quantity), float(take_profit), float(stop_loss))

    #TWAP Order
    elif order_type == "TWAP":
        total_quantity = input("Enter total quantity: ").strip()
        slices = input("Enter number of slices (default 5): ").strip() or "5"
        interval = input("Enter interval (in seconds, default 10): ").strip() or "10"
        if not (validate_positive_float(total_quantity) and slices.isdigit() and interval.isdigit()):
            print("Invalid inputs.")
            sys.exit(1)
        result = place_twap_order(
            symbol,
            side,
            float(total_quantity),
            int(slices),
            int(interval)
        )

    #Grid Orders
    elif order_type == "GRID":
        base_price = input("Enter base price: ").strip()
        grid_size = input("Enter number of grid levels: ").strip()
        price_step = input("Enter price step between levels: ").strip()
        quantity = input("Enter quantity per order: ").strip()
        if not (validate_positive_float(base_price) and grid_size.isdigit() and validate_positive_float(price_step) and validate_positive_float(quantity)):
            print("Invalid inputs.")
            sys.exit(1)
        result = place_grid_orders(
            symbol,
            float(base_price),
            int(grid_size),
            float(price_step),
            float(quantity)
        )

    #Display result
    print("\nOrder Result:")
    if isinstance(result, list):
        for r in result:
            print(r)
    elif isinstance(result, dict):
        for k, v in result.items():
            print(f"{k}: {v}")
    else:
        print(result)


if __name__ == "__main__":
    cli_main()
