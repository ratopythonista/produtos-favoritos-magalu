from loguru import logger

from produtos_favoritos_magalu.services.database import Database


def test_database():
    db = Database()
    logger.debug(db)

def test_customer_database():
    custormer = Customer()
    logger.debug(custormer)