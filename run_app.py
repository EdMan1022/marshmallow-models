from dumb_app.extensions import db
from dumb_app.app import create_app
from dumb_app.config import LocalConfig
from dumb_app.models.user import User


config = LocalConfig()
app = create_app(config, db)


if __name__ == "__main__":
    app.run()

