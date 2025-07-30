# import hmac
# import hashlib
# import time
# import requests
# from urllib.parse import urlencode
# from config import API_KEY, API_SECRET, BASE_URL
# from logger import get_logger

# logger = get_logger("core")

# class BinanceFuturesREST:
#     def __init__(self):
#         self.api_key = API_KEY
#         self.api_secret = API_SECRET.encode()
#         self.base_url = BASE_URL

#     def _timestamp(self):
#         return int(time.time() * 1000)

#     def _sign(self, data: dict):
#         query_string = urlencode(data)
#         signature = hmac.new(self.api_secret, query_string.encode(), hashlib.sha256).hexdigest()
#         return f"{query_string}&signature={signature}"

#     def _headers(self):
#         return {"X-MBX-APIKEY": self.api_key}
    
#     def _dict_to_query_string(self, data: dict) -> str:
#         return "&".join([f"{key}={data[key]}" for key in sorted(data)])
    
#     def get_server_time(self):
#         """
#         Fetch server time from Binance Futures API.
#         """
#         url = self.base_url + "/fapi/v1/time"
#         try:
#             response = requests.get(url, timeout=5)
#             response.raise_for_status()
#             return response.json().get("serverTime")
#         except requests.exceptions.RequestException as e:
#             logger.error(f"Failed to get server time: {e}")
#             return None

#     def place_order(self, data: dict):
#         endpoint = "/fapi/v1/order"
#         data["timestamp"] = self._timestamp()
#         signed_data = self._sign(data)
#         url = f"{self.base_url}{endpoint}?{signed_data}"
#         try:
#             response = requests.post(url, headers=self._headers())
#             logger.info(f"Order placed: {response.json()}")
#             return response.json()
#         except Exception as e:
#             logger.error(f"Order failed: {e}")
#             return {"error": str(e)}

import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import API_KEY, API_SECRET, BASE_URL
from logger import get_logger

logger = get_logger()

class BinanceFuturesREST:
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET.encode()
        self.base_url = BASE_URL

    def _get_timestamp(self):
        try:
            server_time = requests.get(f"{self.base_url}/fapi/v1/time").json()["serverTime"]
            return server_time
        except Exception as e:
            logger.error(f"Timestamp fetch failed: {e}")
            raise

    def _sign(self, data: dict):
        query_string = urlencode(data)
        signature = hmac.new(self.api_secret, query_string.encode(), hashlib.sha256).hexdigest()
        return f"{query_string}&signature={signature}"

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }

    def place_order(self, payload):
        url = self.base_url + "/fapi/v1/order"
        signed_data = self._sign(payload)
        try:
            response = requests.post(url, headers=self._headers(), params=signed_data)
            data = response.json()
            logger.info(f"Order placed: {data}")
            return data
        except Exception as e:
            logger.error(f"Order placement error: {e}")
            return {"error": str(e)}
