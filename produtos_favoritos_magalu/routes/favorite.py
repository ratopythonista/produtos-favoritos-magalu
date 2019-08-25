from flask import request
from flasgger import swag_from
from flask_restful import Resource

from produtos_favoritos_magalu.routes.responses import Response
from produtos_favoritos_magalu.services.luizalabs import get_product
from produtos_favoritos_magalu.services.database import Favorite as FavoriteDB


class Favorite(Resource):
    def get(self):
        customer_email = request.args.get("customer_email")
        favorite, products = FavoriteDB(), list()
        for product_id in favorite.get(customer_email):
            product = get_product(product_id)
            if product:
                products.append(product)
        return Response.info(products)

    def post(self):
        favorite_info, favorite = request.json, FavoriteDB()
        if all(map(favorite_info.get, ['email', 'product_id'])):
            if favorite.insert(favorite_info['email'], favorite_info['product_id']):
                return Response.success()
            else:
                return Response.error('favorite error')
        else:
            return Response.invalid_format()

    def delete(self):
        favorite_info, favorite = request.json, FavoriteDB()
        if all(map(favorite_info.get, ['email', 'product_id'])):
            if favorite.delete(favorite_info['email'], favorite_info['product_id']):
                return Response.success()
            else:
                return Response.error('delete error')
        else:
            return Response.invalid_format()    
    