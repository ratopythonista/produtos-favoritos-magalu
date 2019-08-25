from flask import request
from loguru import logger
from flasgger import swag_from
from flask_restful import Resource

from produtos_favoritos_magalu.services.database import Customer as CustomerDB
from produtos_favoritos_magalu.routes.responses import Response


class Customer(Resource):
    def get(self):
        customer_email = request.args.get("customer_email")
        customer = CustomerDB()
        if not customer_email:
            return Response.info(list(customer.find_all()))
        else:
            customer_info = customer.find(customer_email)
            if not customer_info:
                return Response.customer_not_found()
            else:
                return Response.info(customer_info)

    def post(self):
        customer_info, customer = request.json, CustomerDB()
        if all(map(customer_info.get, ['email', 'name'])):
            if customer.insert(customer_info['email'], customer_info['name']):
                return Response.create_success()
            else:
                return Response.insert_error()
        else:
            return Response.invalid_format()

