from dumb_app.extensions import ma
from dumb_app.models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

