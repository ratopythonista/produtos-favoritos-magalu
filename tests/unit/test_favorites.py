from produtos_favoritos_magalu import app


client = app.test_client()


def test_list_favorite():
    response = client.get('/api/favorite/?customer_email=rodrigoara27@gmail.com')
    assert response.status_code == 200
    assert 'response' in response.json
    assert type(response.json['response']) is list


def test_insert_favorite():
    # Criação do Usuário
    json = {"email":"rodrigoara27@gmail.com", "name":"Rodrigo Guimarães Araújo"}
    response = client.post('/api/customer/', json=json)

    # Inserção de Favorito
    json = {'email':'rodrigoara27@gmail.com', 'product_id':'958ec015-cfcf-258d-c6df-1721de0ab6ea'}
    response = client.post('/api/favorite/', json=json)

    assert response.status_code == 200

    # Exclusão do Usuário
    json = {"email":"rodrigoara27@gmail.com"}
    response = client.delete('/api/customer/', json=json)