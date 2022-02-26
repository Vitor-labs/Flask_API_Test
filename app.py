from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fone = db.Column(db.String(100))

    def __init__(self, name, password, email, fone):
        self.name = name
        self.password = password
        self.email = email
        self.fone = fone

    def __repr__(self):
        return 'User {} | @{} | Email: {}'.format(self.id, self.name, self.email)


name_put_args = reqparse.RequestParser()
name_put_args.add_argument(
    "name", type=str, required=True, help="Name cannot be blank!")
name_put_args.add_argument(
    "password", type=str, required=True, help="Password cannot be blank!")
name_put_args.add_argument(
    "email", type=str, required=True, help="Email cannot be blank!")
name_put_args.add_argument("fone", type=str)

name_update_args = reqparse.RequestParser()
name_update_args.add_argument(
    "name", type=str, required=True, help="Name cannot be blank!")
name_update_args.add_argument(
    "password", type=str, required=True, help="Password cannot be blank!")
name_update_args.add_argument(
    "email", type=str, required=True, help="Email cannot be blank!")
name_update_args.add_argument("fone", type=str)

resources = {
    'id': fields.Integer,
    'name': fields.String,
    'password': fields.String,
    'Email': fields.String,
    'fone': fields.String
}


class UserList(Resource):
    @marshal_with(resources)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user
        else:
            abort(404, message="User {} doesn't exist".format(user_id))

    @marshal_with(resources)
    def put(self, user_id):
        args = name_put_args.parse_args()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            user.name = args['name']
            user.password = args['password']
            user.email = args['email']
            user.fone = args['fone']

            db.session.commit()
            return user
        else:
            abort(404, message="User {} already exist".format(user_id))

    @marshal_with(resources)
    def patch(self, user_id):
        args = name_put_args.parse_args()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User {} doesn't exist, cannot update".format(user_id))
        else:
            if args['name']:
                user.name = args['name']
            if args['password']:
                user.password = args['password']
            if args['email']:
                user.email = args['email']
            if args['fone']:
                user.fone = args['fone']

        db.session.commit()
        return user

    @marshal_with(resources)
    def post(self):
        args = name_put_args.parse_args()
        user = User(**args)
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(resources)
    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        else:
            abort(404, message="User {} doesn't exist".format(user_id))


api.add_resource(UserList, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
