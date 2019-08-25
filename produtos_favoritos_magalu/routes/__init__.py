import time

from loguru import logger
from flask import request

from produtos_favoritos_magalu.routes.customer import Customer


def add_resources(api):
    api.add_resource(Customer, '/api/customer/')


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    resp_time = time.time() - request.start_time
    logger.info(f"Response time: {resp_time}s")
    return response


def record_request_data(response):
    info = f"{request.method} on {request.path} returns {response.status_code}"
    logger.info(info)
    return response


def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(record_request_data)
    app.after_request(stop_timer)