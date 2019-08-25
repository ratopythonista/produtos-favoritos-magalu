import types

from loguru import logger

from produtos_favoritos_magalu.services.luizalabs import (
    list_products, get_product
)


def test_product_list():
    product_list = list_products()
    logger.debug(product_list)
    assert type(product_list) == types.GeneratorType


def test_get_product():
    product = get_product('1579762e-cfc3-5f20-afb7-8208ea92cbd1')
    attributes = ['price', 'image', 'brand', 'id', 'title']
    logger.debug(product)
    assert all(map(product.get, attributes))
