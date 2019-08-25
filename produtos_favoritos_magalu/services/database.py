from loguru import logger
from pymongo import MongoClient

from produtos_favoritos_magalu.config import (
    MONGO_DB, MONGO_HOST, MONGO_PASS, MONGO_PORT, MONGO_USER
)

class Database():
    def __init__(self):
        URI = f'{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
        self.client = MongoClient(f'mongodb://{URI}?retryWrites=false')
        self.db = self.client.get_database()
    
    def __del__(self):
        self.client.close()


class Customer(Database):
    """ Classe destinada as funções para manter Cliente """

    def __init__(self):
        super().__init__()
    
    def find(self, email:str) -> dict:
        """ Busca por um cliente, utilizando seu email """

        return self.db.customers.find_one({'email':email}, {'_id':0})

    def insert(self, email:str, name:str) -> bool:
        """ Insere um novo cliente na base """

        if self.find(email):
            return False
        self.db.customers.insert_one({'email':email, 'name':name})
        return True

    def find_all(self):
        """ Busca todos os clientes """

        return self.db.customers.find({}, {'_id':0})

    def update(self, email:str, new_data:dict) -> int:
        """ Altera informações do cliente """

        if 'email' in new_data and self.find(new_data['email']):
            return False

        return self.db.customers.update_one({'email':email}, 
            {'$set': new_data}).modified_count

    def delete(self, email:str):
        """ Remove o cliente do banco de dados """

        return self.db.customers.delete_one({'email':email}).deleted_count



class Favorite(Database):
    """ Classe destinada as funções para manter Favoritos de Clientes """

    def __init__(self):
        super().__init__()

    def insert(self, email:str, product_id:str) -> bool:
        customer = self.find(email)
        if not customer:
            return False
        favorites_products = customer.get('favorites', set())
        favorites_products.add(product_id)
        self.db.customers.update({'email':email}, 
            {'$set': {'favorites':favorites_products}})
        return True