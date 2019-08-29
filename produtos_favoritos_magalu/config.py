import os

from loguru import logger


MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASS = os.environ.get('MONGO_PASS')
MONGO_DB = os.environ.get('MONGO_DB')
SECRET = os.environ.get('SECRET')

if not all([MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASS, MONGO_DB]):
    logger.warning(f'Not all env variables are seted!')