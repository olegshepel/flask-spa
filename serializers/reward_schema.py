"""
Reward Serializer Class
"""


from flask_marshmallow import Marshmallow

from app import app
from models import Reward

ma = Marshmallow(app)


class RewardSchema(ma.SQLAlchemyAutoSchema):
    """Reward Serializer"""
    class Meta:
        model = Reward
