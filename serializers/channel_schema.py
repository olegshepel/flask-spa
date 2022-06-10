"""
Channel Serializer Class
"""


from flask_marshmallow import Marshmallow

from app import app
from models import Channel

ma = Marshmallow(app)


class ChannelSchema(ma.SQLAlchemyAutoSchema):
    """Channel Serializer"""
    class Meta:
        model = Channel
