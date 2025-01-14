import json
import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.decode() == "API is healthy!"


def test_predict(client):
    sample_input = {
        "store_id": 1,
        "day_of_week": 2,
        "promo": 1,
        "state_holiday": "0",
        "school_holiday": 0,
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert "prediction" in response_data
