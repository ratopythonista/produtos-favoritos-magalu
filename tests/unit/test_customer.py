from produtos_favoritos_magalu import app

from loguru import logger

client = app.test_client()
token = client.post('/api/validate/', json={"customer_email":"rodrigoara27@gmail.com"}).json['response']

def test_list():
    response = client.get('/api/customer/')
    assert response.status_code == 200
    assert 'response' in response.json
    assert type(response.json['response']) == list


def test_insert():
    json = {
        "email":"ratopythonista@gmail.com", 
        "name":"Rato Pythonista",
        "token":token
    }

    response = client.post('/api/customer/', json=json)
    assert response.status_code == 201
    response = client.post('/api/customer/', json=json)
    assert response.status_code == 500


def test_find():
    param = '?customer_email=ratopythonista@gmail.com'
    response = client.get(f'/api/customer/{param}')
    assert response.status_code == 200
    assert 'response' in response.json
    assert all(map(response.json['response'].get, ['email', 'name']))


def test_delete():
    json = {"email":"ratopythonista@gmail.com", "token":token}

    response = client.delete('/api/customer/', json=json)
    assert response.status_code == 200
    response = client.delete('/api/customer/', json=json)
    assert response.status_code == 500


def test_update():
    upd_json = {
        "email": "ratopythonista@gmail.com", 
        "att":{"email":"outroemail@gmail.com"},
        "token":token
    }
    del_json = {"email":"outroemail@gmail.com", "token":token}
    ins_json = {
        "email":"ratopythonista@gmail.com", 
        "name":"Rato Pythonista",
        "token":token
    }
    ins_json_2 = {
        "email":"outroemail@gmail.com", 
        "name":"Outra Pessoa",
        "token":token
    }

    # Se já existe alguem com o novo email
    response = client.post('/api/customer/', json=ins_json)
    response = client.post('/api/customer/', json=ins_json_2)
    response = client.put('/api/customer/', json=upd_json)
    assert response.status_code == 500

    # Se é possivel realizar a mudança
    response = client.delete('/api/customer/', json=del_json)
    response = client.put('/api/customer/', json=upd_json)
    assert response.status_code == 200

    # Se o email informado não existe
    response = client.put('/api/customer/', json=upd_json)
    assert response.status_code == 500

    # limpando os testes
    response = client.delete('/api/customer/', json=del_json)