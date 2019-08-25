import sys

from flask import Flask
from loguru import logger
from flask_cors import CORS
from flasgger import Swagger
from flask_restful import Api

from produtos_favoritos_magalu.routes import add_resources, setup_metrics


logger.add("produtos_favoritos_magalu.log", rotation="500 MB")

template = {
    "swagger": "2.0",
    "info": {
        "title": "Desafio Técnico - LuizaLabs/Magalu",
        "description": "",
        "version": "0.1.0"
    },
}

app = Flask(__name__)
CORS(app)
api = Api(app)
swagger = Swagger(app, template=template)

add_resources(api)
setup_metrics(app)

@app.route('/')
def index():
    return 'Application is alive', 200

