def test_health_check(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_cep_valid_format_with_dash(client):
    response = client.get("/api/v1/cep/01001-000")
    assert response.status_code == 200
    data = response.json()
    assert "cep" in data
    assert "street" in data


def test_get_cep_valid_format_numeric(client):
    response = client.get("/api/v1/cep/01001000")
    assert response.status_code == 200


def test_get_cep_invalid_format(client):
    response = client.get("/api/v1/cep/abcde-fgh")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid CEP"}


def test_get_cep_invalid_short(client):
    response = client.get("/api/v1/cep/123")
    assert response.status_code == 400


def test_get_cep_invalid_too_long(client):
    response = client.get("/api/v1/cep/123456789012")
    assert response.status_code == 400


def test_swagger_docs_accessible(client):
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_schema(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "CEP API"
    assert schema["info"]["version"] == "1.0.0"
