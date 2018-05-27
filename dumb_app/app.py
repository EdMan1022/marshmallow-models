from flask import Flask
from dumb_app.blueprints.core import core


def create_app(config, db):

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(core)
    return app

