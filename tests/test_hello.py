from fastapi.testclient import TestClient
from app.main import app

client: TestClient = TestClient(app)


def test_get_hello() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_post_hello() -> None:
    response = client.post("/", json={"name": "Gemini"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, Gemini"}


def test_post_hello_invalid() -> None:
    response = client.post("/", json={"invalid": "data"})
    assert response.status_code == 422
