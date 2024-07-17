def test_create_post(client, auth_headers):
    response = client.post('/posts', json={'title': 'Test Post', 'content': 'This is a test post.'}, headers=auth_headers)
    assert response.status_code == 201

def test_get_all_posts(client, auth_headers):
    response = client.get('/posts', headers=auth_headers)
    assert response.status_code == 200

def test_update_post(client, auth_headers):
    response = client.post('/posts', json={'title': 'Test Post', 'content': 'This is a test post.'}, headers=auth_headers)
    post_id = response.json['post_id']
    response = client.put(f'/posts/{post_id}', json={'title': 'Updated Post', 'content': 'Updated content.'}, headers=auth_headers)
    assert response.status_code == 200

def test_delete_post(client, auth_headers):
    response = client.post('/posts', json={'title': 'Test Post', 'content': 'This is a test post.'}, headers=auth_headers)
    post_id = response.json['post_id']
    response = client.delete(f'/posts/{post_id}', headers=auth_headers)
    assert response.status_code == 204
