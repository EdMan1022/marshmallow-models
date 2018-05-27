from os import environ

local_db_uri = environ['local_db_uri']
dev_db_uri = environ['dev_db_uri']
test_db_uri = environ['test_db_uri']
production_db_uri = environ['production_db_uri']


class BaseConfig(object):

    ENV = "production"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = environ['local_db_uri']
    ENV = "development"
    DEBUG = True


