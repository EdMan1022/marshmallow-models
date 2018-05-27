from flask import Blueprint, render_template

from dumb_app.extensions import db
from dumb_app.models.user import User

core = Blueprint('core', 'core')


@core.route('/')
def home():
    return 'Hello World!'


@core.route('/users')
def list_users():
    users = User.query.all()

    return render_template('users.html', users=users)
