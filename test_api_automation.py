import requests 

URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f'{URL}/posts/1')
    assert response.status_code == 200 
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_post():
    payload = {"title": "test", "body": "its a test", "userId": 1}
    response = requests.post(f'{URL}/posts', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]

def test_update_post():
     payload = {"id": 1, "title": "Updated", "body": "Updated body", "userId": 1}
     response = requests.put(f'{URL}/posts/1', json=payload)
     assert response.status_code == 200
     data = response.json()
     assert data["title"] == payload['title']

def test_delete_post():
    response = requests.delete(f'{URL}/posts/1')
    assert response.status_code == 200
    











