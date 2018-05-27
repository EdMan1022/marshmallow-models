from dumb_app.extensions import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name: str, id: int=None):

        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.id}: {self.name.capitalize()}"
