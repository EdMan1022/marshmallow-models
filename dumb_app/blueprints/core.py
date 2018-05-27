from flask import Blueprint

core = Blueprint('core', 'core')


@core.route('/')
def home():
    return 'Hello World!'
