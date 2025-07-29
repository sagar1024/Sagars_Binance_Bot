import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
TESTNET = os.getenv("BINANCE_TESTNET", "false").lower() == "true"

BASE_URL = "https://testnet.binancefuture.com" if TESTNET else "https://fapi.binance.com"
VALID_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
