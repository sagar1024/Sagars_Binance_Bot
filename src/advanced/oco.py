#Binance Futures does not support native OCO, but we'll simulate it with two separate orders

from binance.client import Client
from src.config import API_KEY, API_SECRET, TESTNET
from src.utils import validate_symbol, validate_quantity, validate_price
from src.logger import log_info, log_error

def place_oco_order(symbol, quantity, tp_price, sl_price):
    try:
        client = Client(API_KEY, API_SECRET, testnet=TESTNET)
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        tp_price = validate_price(tp_price)
        sl_price = validate_price(sl_price)

        # Take profit
        tp_order = client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="LIMIT",
            quantity=quantity,
            price=tp_price,
            timeInForce="GTC"
        )

        # Stop loss
        sl_order = client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="STOP_MARKET",
            stopPrice=sl_price,
            quantity=quantity
        )

        log_info(f"OCO simulated. TP: {tp_order}, SL: {sl_order}")
        print("✅ OCO (TP & SL) Orders Placed.")
    except Exception as e:
        log_error(f"OCO order error: {e}")
        print(f"❌ Error: {e}")
