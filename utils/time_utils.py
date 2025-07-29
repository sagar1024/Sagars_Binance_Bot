import requests

def get_binance_server_time():
    try:
        response = requests.get("https://testnet.binancefuture.com/fapi/v1/time", timeout=2)
        return response.json()["serverTime"]
    except Exception as e:
        raise Exception(f"Failed to fetch server time: {e}")
