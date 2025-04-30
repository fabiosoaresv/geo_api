import pytest
from app.services.geo_api_service import GeoApiService
from unittest.mock import patch

@pytest.fixture
def geo_api_service():
    return GeoApiService()

@patch('app.services.geo_api_service.requests.get')
def test_get_weather_success(mock_get, geo_api_service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": [{"city": "Piraju", "weather": "sunny"}]
    }

    result = geo_api_service.get_weather("Piraju")

    assert result == {"city": "Piraju", "weather": "sunny"}
    mock_get.assert_called_once()
