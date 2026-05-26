from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_mission() -> None:
    response = client.get('/mission')
    assert response.status_code == 200
    body = response.json()
    assert body['name'] == 'DES'
    assert body['phase'] == 'phase-1-foundation'
