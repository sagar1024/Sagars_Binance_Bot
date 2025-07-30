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
