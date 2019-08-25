from produtos_favoritos_magalu import app


client = app.test_client()


def test_list():
    response = client.get('/api/customer/')
    assert response.status_code == 200
    assert 'response' in response.json
    assert type(response.json['response']) == list

def test_find():
