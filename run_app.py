from dumb_app.extensions import db, api, ma
from dumb_app.app import create_app
from dumb_app.config import LocalConfig
from dumb_app.models.user import User


config = LocalConfig()
app = create_app(config, db, api, ma)


if __name__ == "__main__":
    app.run()

