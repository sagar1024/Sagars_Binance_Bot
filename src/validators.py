def validate_symbol(symbol: str):
    return symbol.isalnum() and len(symbol) >= 6

def validate_side(side: str):
    return side in ["BUY", "SELL"]

def validate_order_type(order_type: str):
    return order_type in ["MARKET", "LIMIT", "STOP_LIMIT", "OCO", "TWAP", "GRID"]

def validate_positive_float(value):
    try:
        return float(value) > 0
    except:
        return False
