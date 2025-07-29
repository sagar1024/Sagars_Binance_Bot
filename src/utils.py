from src.config import VALID_SYMBOLS

def validate_symbol(symbol):
    symbol = symbol.upper()
    if symbol not in VALID_SYMBOLS:
        raise ValueError(f"Invalid symbol: {symbol}")
    return symbol

def validate_quantity(quantity):
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError
        return q
    except:
        raise ValueError("Quantity must be a positive number")

def validate_price(price):
    try:
        p = float(price)
        if p <= 0:
            raise ValueError
        return p
    except:
        raise ValueError("Price must be a positive number")
