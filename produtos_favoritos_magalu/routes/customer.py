from flask import request
from flasgger import swag_from
from flask_restful import Resource

from produtos_favoritos_magalu.routes.responses import Response
from produtos_favoritos_magalu.services.database import Customer as CustomerDB


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
                return Response.error('insert error')
        else:
            return Response.invalid_format()

    def delete(self):
        customer_info, customer = request.json, CustomerDB()
        if all(map(customer_info.get, ['email'])):
            if customer.delete(customer_info['email']):
                return Response.success()
            else:
                return Response.error('delete error')
        else:
            return Response.invalid_format()

    def put(self):
        customer_info, customer = request.json, CustomerDB()
        if all(map(customer_info.get, ['email', 'att'])):
            if customer.update(customer_info['email'], customer_info['att']):
                return Response.success()
            else:
                return Response.error('update error')
        else:
            return Response.invalid_format()
