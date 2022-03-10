from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import configure_db, UserModel, AccountModel

app = Flask(__name__)
api = Api(app)

db = configure_db(app)

# ============================= Resources =====================================
user_put_args = reqparse.RequestParser()
user_put_args.add_argument(
    "username", type=str, required=True, help="Username is required")
user_put_args.add_argument(
    "email", type=str, required=True, help="Email is required")
user_put_args.add_argument(
    "fone", type=str, required=True, help="Fone is required")

user_update_args = reqparse.RequestParser()
user_update_args.add_argument(
    "username", type=str, required=False, help="Username is required")
user_update_args.add_argument(
    "email", type=str, required=False, help="Email is required")
user_update_args.add_argument(
    "fone", type=str, required=False, help="Fone is required")

user_resourse_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "fone": fields.String
}
# ============================================================================
account_put_args = reqparse.RequestParser()
account_put_args.add_argument('username', type=str, required=True,
                              help="username cannot be left blank!")
account_put_args.add_argument('password', type=str, required=True,
                              help="password cannot be left blank!")
account_put_args.add_argument('user_id', type=int, required=True,
                              help="user id cannot be left blank!")

account_update_args = reqparse.RequestParser()
account_update_args.add_argument('username', type=str, required=True,
                                 help="username cannot be left blank!")
account_update_args.add_argument('password', type=str, required=True,
                                 help="password cannot be left blank!")
account_update_args.add_argument('user_id', type=int, required=True,
                                 help="user id cannot be left blank!")

account_resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'user_id': fields.Integer,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}
# ============================================================================


class User(Resource):
    @marshal_with(user_resourse_fields)
    def get(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @marshal_with(user_resourse_fields)
    def put(self, user_id):
        args = user_put_args.parse_args()
        result = UserModel.query.filter_by(id=user_id).first()
        if result:
            abort(409, message="User id taken...")

        user = User(args['name'], args['email'], args['fone'])

        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(user_resourse_fields)
    def post(self, user_id):
        args = user_update_args.parse_args()
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        result.username = args['username']
        result.email = args['email']
        result.fone = args['fone']

        db.session.commit()
        return result, 201

    @marshal_with(user_resourse_fields)
    def patch(self, user_id):
        args = user_update_args.parse_args()
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['email']:
            result.email = args['email']
        if args['likes']:
            result.fone = args['fone']

        db.session.commit()

        return result

    def delete(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User doesn't exist, cannot delete")

        db.session.delete(result)
        db.session.commit()
        return "", 204


api.add_resource(User, "/user/<int:user_id>")

# ============================================================================


class Account(Resource):
    @marshal_with(account_resource_fields)
    def get(self, account_id):
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Could not find account with that id")
        return result

    @marshal_with(account_resource_fields)
    def put(self, account_id):
        args = account_put_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if result:
            abort(409, message="Account id taken...")

        account = AccountModel(
            args['username'], args['password'], args['user_id'])

        db.session.add(account)
        db.session.commit()
        return account, 201

    @marshal_with(account_resource_fields)
    def patch(self, account_id):
        args = account_update_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Account doesn't exist, cannot update")

        if args['username']:
            result.username = args['username']
        if args['password']:
            result.password = args['password']
        if args['user_id']:
            result.user_id = args['user_id']

        db.session.commit()

        return result

    def delete(self, account_id):
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Account doesn't exist, cannot delete")

        db.session.delete(result)
        db.session.commit()
        return "", 204


api.add_resource(Account, "/account/<int:account_id>")

if __name__ == "__main__":
    app.run(debug=True)
