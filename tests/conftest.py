# tests/conftest.py

import pytest
from app import create_app, db
from app.auth.models import User
from app.blog_post.models import BlogPost

@pytest.fixture(scope='module')
def app():
    app = create_app('testing')
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def auth_headers(client):
    response = client.post('/auth/register', json={'email': 'testuser@example.com', 'password': 'testpass'})
    token = response.json['auth_token']
    return {'Authorization': f'Bearer {token}'}
