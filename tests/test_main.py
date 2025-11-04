from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_api():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtract_api():
    response = client.get("/subtract?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply_api():
    response = client.get("/multiply?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_divide_api():
    response = client.get("/divide?a=6&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_divide_by_zero_api():
    response = client.get("/divide?a=5&b=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"
