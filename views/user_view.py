from flask import jsonify
from flask_restful import Resource, fields, marshal_with, reqparse
from models.user_model import UserModel
from models import db
from werkzeug.security import generate_password_hash, check_password_hash
from utils import abort_if_doesnt_exist

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'password': fields.String,
    'admin': fields.Boolean,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}

class User(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        abort_if_doesnt_exist(UserModel, user_id)
        user = UserModel.query.filter_by(id=user_id).first()
        return user

    def delete(self, user_id):
        abort_if_doesnt_exist(UserModel, user_id)
        user = UserModel.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return ''

    @marshal_with(resource_fields)
    def put(self, user_id):
        abort_if_doesnt_exist(UserModel, user_id)
        user = UserModel.query.filter_by(id=user_id).first()
        parser_update = reqparse.RequestParser()
        parser_update.add_argument('name', type=str)
        args = parser_update.parse_args()
        if 'name' in args:
            user.name = args['name']
        db.session.commit()
        return user, 201


class UserList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(resource_fields)
    def post(self):
        parser_create = reqparse.RequestParser()
        parser_create.add_argument('name', type=str, help="Name is required", required=True)
        parser_create.add_argument('password', help="Password is required", type=str)
        args = parser_create.parse_args()
        hashed_password = generate_password_hash(
            args['password'], method='sha256')
        new_user = UserModel(
            name=args['name'], password=hashed_password, admin=False)
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201
