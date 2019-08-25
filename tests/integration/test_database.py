from loguru import logger

from produtos_favoritos_magalu.services.database import Database


def test_database():
    db = Database()
    logger.debug(db)