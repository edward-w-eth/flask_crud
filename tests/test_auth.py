def test_hello(client):
    response = client.get("/")
    print(response)

def test_register(client):
    response = client.post('/auth/register', json={'email': 'test@example.com', 'password': 'testpass'})
    assert response.status_code == 201
    assert 'auth_token' in response.json

def test_login(client):
    response = client.post('/auth/login', json={'email': 'test@example.com', 'password': 'testpass'})
    assert response.status_code == 200
    assert 'auth_token' in response.json

def test_login_failed(client):
    response = client.post('/auth/login', json={'email': 'test1@example.com', 'password': 'testpass'})
    assert response.status_code == 404
