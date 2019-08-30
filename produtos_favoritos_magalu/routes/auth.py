from datetime import datetime, timedelta

import jwt
from flask import request
from flasgger import swag_from
from flask_restful import Resource

from produtos_favoritos_magalu.config import SECRET
from produtos_favoritos_magalu.routes.responses import Response
from produtos_favoritos_magalu.services.database import Customer as CustomerDB


class Auth(Resource):

    @swag_from('../../docs/auth.yml')
    def post(self):
        customer_email = request.json['customer_email']
        if CustomerDB().find(customer_email):
            token = jwt.encode({
                'exp':datetime.utcnow()+timedelta(minutes=5),
                'email':customer_email
            }, SECRET, algorithm='HS256')
            return Response.info(token.decode('utf-8'))
        else:
            return Response.error('invalid user')
