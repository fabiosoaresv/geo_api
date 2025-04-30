import unittest
from fastapi.testclient import TestClient
from app.main import app
import pytest
from unittest.mock import patch

client = TestClient(app)

@patch("app.controllers.geo_api_controller.GeoApiService")
def test_post_weather_success(mock_service):
    mock_instance = mock_service.return_value
    mock_instance.get_weather.return_value = {"city": "Piraju", "weather": "sunny"}

    response = client.post("/weather/Piraju")

    assert response.status_code == 200
    assert response.json() == {"city": "Piraju", "weather": "sunny"}
    mock_instance.get_weather.assert_called_once_with("Piraju", unittest.mock.ANY)
