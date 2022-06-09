from flask_marshmallow import Marshmallow

from app import app
from models import Channel, Reward, User

ma = Marshmallow(app)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class RewardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward


class ChannelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Channel
