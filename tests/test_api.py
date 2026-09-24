from fastapi.testclient import TestClient
from trafficbrain.api.server import app
def test_health(): assert TestClient(app).get('/health').status_code==200
def test_simulate():
    r=TestClient(app).get('/simulate?steps=5'); assert r.status_code==200; assert r.json()['steps']==5
