#OCO (One Cancels the Other) orders are not supported on Binance Futures via the /fapi/v1/order endpoint
#But we can simulate it manually by placing two orders: a Take-Profit and Stop-Loss, and cancelling the other once one gets filled
#This implementation simulates OCO logic (manual pseudo-OCO).

from binance_client import BinanceFuturesREST
from logger import get_logger

logger = get_logger()
client = BinanceFuturesREST()

def place_oco_simulated(symbol, side, quantity, take_profit_price, stop_loss_price):
    opposite_side = "SELL" if side == "BUY" else "BUY"

    #Take-Profit Limit Order
    tp_payload = {
        "symbol": symbol,
        "side": opposite_side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": take_profit_price,
        "timeInForce": "GTC",
        "timestamp": client._get_timestamp(),
        "recvWindow": 10000
    }

    #Stop-Loss Market Order
    sl_payload = {
        "symbol": symbol,
        "side": opposite_side,
        "type": "STOP_MARKET",
        "stopPrice": stop_loss_price,
        "quantity": quantity,
        "timestamp": client._get_timestamp(),
        "recvWindow": 10000
    }

    tp_result = client.place_order(tp_payload)
    sl_result = client.place_order(sl_payload)

    logger.info("Simulated OCO: Take-Profit and Stop-Loss submitted")

    return {"take_profit_result": tp_result, "stop_loss_result": sl_result}
