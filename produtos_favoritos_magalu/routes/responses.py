class Response():

    @staticmethod
    def success():
        return {'message':'success'}, 200

    @staticmethod
    def info(value):
        return {'message':'success', 'response':value}, 200

    @staticmethod
    def invalid_format():
        return {'message':'invalid json format'}, 406

    @staticmethod
    def error(message):
        return {'message':message}, 500

    @staticmethod
    def customer_not_found():
        return {'message':'customer not found'}, 404

    @staticmethod
    def create_success():
        return {'message':'success on user creating'}, 201