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


def test_memory_roundtrip() -> None:
    create = client.post('/memory', json={'memory_type': 'project', 'summary': 'Ship voice streaming', 'tags': ['voice', 'phase1']})
    assert create.status_code == 200
    data = client.get('/memory?query=voice')
    assert data.status_code == 200
    items = data.json()['items']
    assert len(items) >= 1
    assert any(item['summary'] == 'Ship voice streaming' for item in items)


def test_agent_plan() -> None:
    response = client.post('/agent/plan', json={'message': 'Continue building DES voice pipeline.'})
    assert response.status_code == 200
    body = response.json()
    assert len(body['plan']) >= 4
    assert body['plan'][0]['role'] == 'architect'
