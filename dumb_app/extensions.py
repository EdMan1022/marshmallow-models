from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

# Initialize a Declarative Base object for the database
db = SQLAlchemy()

api = Api()

ma = Marshmallow()
