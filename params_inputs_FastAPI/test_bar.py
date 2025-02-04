import json
from fastapi.testclient import TestClient

from bar import app

client = TestClient(app)


def test_post():
    data = json.dumps({"value": 10})
    r = client.post("/42?query=5", data=data)
    print(r.json())
    # {'path': 42, 'query': 5, 'body': {'value': 10}}
    assert r.json()["path"] == 42
    assert r.json()["query"] == 5
    assert r.json()["body"] == {"value": 10}

# We don't really need the below function
# invokation, because we can use pytest!
# FastAPI TestClient works with pytest!
'''
if __name__ == '__main__':

    test_post()
'''
