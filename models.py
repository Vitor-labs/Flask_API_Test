from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


def configure_db(app: Flask) -> SQLAlchemy:
    '''
    initialization of SQLAlchemy
    :param app: Flask instance to be used
    :return: None
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return db

# API ACCOUNT & USER MODELS
# ============================================================================


class UserModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fone = db.Column(db.String(30), unique=True)
    account = db.Column(db.Integer, db.ForeignKey('accounts.id'))

    def __init__(self, username, cpf, email, fone):
        self.name = username
        self.cpf = cpf
        self.email = email
        self.fone = fone

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'fone': self.fone
        }


class AccountModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __repr__(self):
        return f'<Account-[{self.id}] {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
