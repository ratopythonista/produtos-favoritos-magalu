import jwt
from loguru import logger

from produtos_favoritos_magalu.config import SECRET
from produtos_favoritos_magalu.services.database import Customer as CustomerDB

def validate_token(token):
    try:
        info = jwt.decode(token.encode('utf-8'), SECRET, algorithm='HS256')
        logger.info(f"Token: {info}")
        return CustomerDB().find(info['email'])
    except jwt.ExpiredSignatureError:
        return False