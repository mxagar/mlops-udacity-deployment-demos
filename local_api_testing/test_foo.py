from fastapi.testclient import TestClient

# Import the app from foo.py
from foo import app

# Instantiate the TestClient with the app
client = TestClient(app)

# Recommendation: write a test for each
# endpoint usage case;
# that facilitates rapid identification of what exactly
# is failing when a test breaks
def test_get_path():
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 42"}

def test_get_path_query():
    r = client.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}

def test_get_malformed():
    r = client.get("/items")
    assert r.status_code != 200
