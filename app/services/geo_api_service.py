import requests, time, pdb, os, httpx
from functools import lru_cache
import pdb

class GeoApiService:
    def __init__(self):
        self.api_url = os.getenv('GEOCODING_API_URL')

    @lru_cache(maxsize=128)
    def get_weather(self, city: str, _ttl_key: int = None):
        if _ttl_key is None:
                _ttl_key = int(time.time() // 60)

        response = requests.get(f"{self.api_url}/search?name={city}&count=1")
        if response.status_code == 200:
            data = response.json()
            return self.__get_result(data)
        else:
            return {"error": "Failed to fetch weather data"}

    @lru_cache(maxsize=128)
    async def get_weather_async(self, city: str, _ttl_key: int = None):
        async with httpx.AsyncClient() as client:
            if _ttl_key is None:
                _ttl_key = int(time.time() // 60)

            response = await client.get(f"{self.api_url}/search?name={city}&count=1")
            if response.status_code == 200:
                data = response.json()
                return self.__get_result(data)
            else:
                return {"error": "Failed to fetch weather data"}

    def __get_result(self, data: dict):
        return data.get('results', [])[0] if data.get('results') else {"error": "No results found"}
