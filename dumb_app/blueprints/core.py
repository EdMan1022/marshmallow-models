from flask import Blueprint, render_template, request
from flask_restful import Resource

from dumb_app.extensions import db, api
from dumb_app.models.user import User
from dumb_app.schema.user_schema import UserSchema

core = Blueprint('core', 'core')


user_schema = UserSchema()


@core.route('/')
def home():
    return 'Hello World!'


@core.route('/users')
def list_users():
    users = User.query.all()

    return render_template('users.html', users=users)


@core.route('/user/', methods=['POST'])
@core.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_route(user_id=None):

    if request.method == 'GET':
        user = User.query.get(int(user_id))
        return user_schema.jsonify(user)

    elif request.method == 'POST':
        new_user = user_schema.load(request.json).data
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    elif request.method == 'PUT':
        old_user = User.query.get(int(user_id))
        new_user = user_schema.load(request.json, instance=old_user).data
        db.session.commit()
        return user_schema.jsonify(new_user)

    elif request.method == 'DELETE':
        old_user = User.query.get(int(user_id))
        db.session.delete(old_user)
        db.session.commit()
        return user_schema.jsonify(old_user)
