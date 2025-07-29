import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

#BASE_URL = os.getenv("BINANCE_API_URL", "https://testnet.binancefuture.com")
BASE_URL = 'https://testnet.binancefuture.com/fapi'

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL
client.API_URL = BASE_URL  #Redundant, but safe
client._timestamp_offset = None
client._sync_request_time = True  #ENABLE TIME SYNC
