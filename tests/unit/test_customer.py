from produtos_favoritos_magalu import app


client = app.test_client()


def test_list():
    response = client.get('/api/customer/')
    assert response.status_code == 200
    assert 'response' in response.json
    assert type(response.json['response']) == list


def test_insert():
    json = {"email":"rodrigoara27@gmail.com", "name":"Rodrigo Guimarães Araújo"}

    response = client.post('/api/customer/', json=json)
    assert response.status_code == 201
    response = client.post('/api/customer/', json=json)
    assert response.status_code == 500


def test_find():
    param = '?customer_email=rodrigoara27@gmail.com'
    response = client.get(f'/api/customer/{param}')
    assert response.status_code == 200
    assert 'response' in response.json
    assert all(map(response.json['response'].get, ['email', 'name']))


def test_delete():
    json = {"email":"rodrigoara27@gmail.com"}

    response = client.delete('/api/customer/', json=json)
    assert response.status_code == 200
    response = client.delete('/api/customer/', json=json)
    assert response.status_code == 500


def test_update():
    upd_json = {
        "email": "rodrigoara27@gmail.com", 
        "att":{"email":"ratopythonista@gmail.com"}
    }
    del_json = {"email":"ratopythonista@gmail.com"}
    ins_json = {
        "email":"rodrigoara27@gmail.com", 
        "name":"Rodrigo Guimarães Araújo"
    }
    ins_json_2 = {
        "email":"ratopythonista@gmail.com", 
        "name":"Rodrigo Guimarães Araújo"
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