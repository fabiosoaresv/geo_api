from app.services.geo_api_service import GeoApiService
from fastapi import APIRouter
import time

geo_api_router = APIRouter()

class GeoApiController:
    @geo_api_router.get("/weather")
    def get_weather():
        return {"weather": "sunny", "temperature": 25}

    @geo_api_router.post("/weather/{city}")
    def get_weather(city: str, _ttl_key: int = None):
        if _ttl_key is None:
            _ttl_key = int(time.time() // 60)

        service = GeoApiController().__geo_api_service()
        return service.get_weather(city, _ttl_key)


    @geo_api_router.post("/async/weather/{city}")
    async def get_weather(city: str, _ttl_key: int = None):
        if _ttl_key is None:
            _ttl_key = int(time.time() // 60)

        service = GeoApiController().__geo_api_service()
        return await service.get_weather_async(city, _ttl_key)

    def __geo_api_service(self):
        return GeoApiService()
