from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_cep():
    response = client.get("/api/v1/cep/01001-000")
    assert response.status_code == 200

def test_get_cep_not_found():
    response = client.get("/api/v1/cep/abcde-fgh")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid CEP"}
