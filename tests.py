from binance.client import Client
from datetime import datetime

client = Client()
server_time = client.futures_time()
local_time = int(datetime.now().timestamp() * 1000)

print(f"Server Time : {server_time['serverTime']}")
print(f"Local Time  : {local_time}")
print(f"Drift (ms)  : {local_time - server_time['serverTime']}")
