"""
User Class
"""


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app import db

association_user_channel_table = Table(
    'user_channel',
    db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('channel_id', Integer, ForeignKey('channel.id'))
)


class User(db.Model):
    """Users"""
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    rewards = relationship('Reward', backref='user')
    channels = relationship('Channel', secondary=association_user_channel_table,
                            backref='users', lazy='dynamic')

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'
