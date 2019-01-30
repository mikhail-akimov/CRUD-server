from project.app import app
import pdb
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_empty(client):
    req = client.get('/todos')
    # pdb.set_trace()
    assert req.data == b'{"todo1": {"task": "build an API"}, "todo2": {"task": "??????"}, "todo3": {"task": "profit!"}}\n'