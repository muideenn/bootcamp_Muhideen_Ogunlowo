
import json
from app import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200

def test_predict_post():
    client = app.test_client()
    payload = {"features": [[1.0, 2.0], [0.5, -1.2]]}
    r = client.post("/predict", data=json.dumps(payload), content_type="application/json")
    assert r.status_code == 200
    data = r.get_json()
    assert "predictions" in data

def test_predict_get_one():
    client = app.test_client()
    r = client.get("/predict/1.5")
    assert r.status_code == 200

def test_predict_get_two():
    client = app.test_client()
    r = client.get("/predict/1.5/-0.2")
    assert r.status_code == 200

def test_plot():
    client = app.test_client()
    r = client.get("/plot")
    assert r.status_code == 200
    assert r.mimetype == "image/png"
