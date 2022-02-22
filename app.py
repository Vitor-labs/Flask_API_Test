from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/hello')


class User(Resource):
    def get(self, user_id):
        return {'user_id': user_id}

    def post(self, user_id):
        return {'user_id': user_id}

    def put(self, user_id):
        return {'user_id': user_id}

    def delete(self, user_id):
        return {'user_id': user_id}


if __name__ == '__main__':
    app.run(debug=True)
