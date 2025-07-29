import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
USE_TESTNET = os.getenv("USE_TESTNET", "True").lower() == "true"

# Base URLs for testnet and mainnet
TESTNET_URL = "https://testnet.binancefuture.com"
MAINNET_URL = "https://fapi.binance.com"

# Initialize client
def get_binance_client():
    client = Client(api_key=API_KEY, api_secret=API_SECRET)
    if USE_TESTNET:
        client.FUTURES_URL = TESTNET_URL
    return client
