import pytest
from main import app
import json

@pytest.fixture(scope='module')
def client():
    with app.test_client() as c:
        yield c


def test_fetch_books(client):
    response = client.get('/api/v1/books')
    assert response.status_code == 200

def test_fetch_book(client):
    response = client.get('/api/v1/book/1')
    assert response.status_code == 200

def test_add_books(client):
    payload = json.dumps({
        "name": "Test Name",
        "title":"Test Book"
    })
    response = client.post('/api/v1/book', headers={"Content-Type": "application/json"}, data=payload)
    assert response.status_code == 200

def test_update_book(client):
    payload = json.dumps({
        "name": "Test Name Updated",
        "title":"Test Book Updated"
    })
    response = client.put('/api/v1/book/1', headers={"Content-Type": "application/json"}, data=payload)
    assert response.status_code == 200

def test_delete_book(client):
    response = client.delete('/api/v1/book/3')
    assert response.status_code == 200
