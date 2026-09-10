from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_success():
    response = client.post("/predict", json={"value": 5.0})
    assert response.status_code == 200
    assert response.json()["prediction"] == 10.0

def test_predict_missing_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "invalid"})
    assert response.status_code == 422
