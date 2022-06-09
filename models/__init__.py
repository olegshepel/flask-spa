"""
Class Models
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app import db

Base = declarative_base()

association_user_channel_table = db.Table('association', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'))
)


class User(db.Model):
    """Users"""
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    rewards = relationship('Reward', backref='user')
    channels = relationship('Channel', secondary=association_user_channel_table, backref='users', lazy='dynamic')

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Channel(db.Model):
    """Channels"""
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Reward(db.Model):
    """Rewards"""
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'
