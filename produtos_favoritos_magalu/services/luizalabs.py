import requests


__URL = 'http://challenge-api.luizalabs.com/api/product/'
    

def list_products() -> list:
    """ Consulta a API da Luiza Labs e retorna a lista de produtos """
    
    page = 1
    while True:
        response = requests.get(__URL + str(page))
        if response.status_code == 404:
            break
        yield response.json().get('products')
        page += 1


def get_product(product_id:str) -> dict:
    """ Consulta a API da Luiza Labs e retorna as informações do produto """

    response = requests.get(__URL + product_id)
    if response.status_code == 404:
        return dict()
    else:
        return response.json()
