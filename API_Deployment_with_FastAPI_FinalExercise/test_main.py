import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# This will pass
def test_post_data_success():
    data = {"feature_1": 1, "feature_2": "test string"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 200

# This will pass, but note that we check we get a 400 status code (error)
def test_post_data_fail():
    data = {"feature_1": -5, "feature_2": "test string"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 400

# To run this:
# pytest
