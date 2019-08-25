from pymongo import MongoClient

from produtos_favoritos_magalu.config import (
    MONGO_DB, MONGO_HOST, MONGO_PASS, MONGO_PORT, MONGO_USER
)

class Database():
    def __init__(self):
        URI = f'{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
        self.client = MongoClient(f'mongodb://{URI}')
        self.db = self.client.get_database()
    
    
    def __del__(self):
        self.client.close()