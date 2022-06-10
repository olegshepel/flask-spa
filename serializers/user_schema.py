"""
User Serializer Class
"""


from flask_marshmallow import Marshmallow

from app import app
from models import User

ma = Marshmallow(app)


class UserSchema(ma.SQLAlchemyAutoSchema):
    """User Serializer"""
    class Meta:
        model = User
