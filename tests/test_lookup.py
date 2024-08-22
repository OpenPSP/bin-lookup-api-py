from fastapi.testclient import TestClient
from bin_lookup_api import app

client = TestClient(app)

def test_lookup_bin_success():
    response = client.get("/lookup/400002")
    assert response.status_code == 200
    assert response.json()["Brand"] == "VISA"

def test_lookup_bin_not_found():
    response = client.get("/lookup/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "BIN not found"}

def test_lookup_bin_invalid_length():
    response = client.get("/lookup/123")
    assert response.status_code == 400
    assert response.json() == {"detail": "BIN must be between 6 and 8 digits"}

def test_lookup_bin_not_numeric():
    response = client.get("/lookup/ABC123")
    assert response.status_code == 400
    assert response.json() == {"detail": "BIN must be a numeric value"}
