"""
Reward Class
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from app import db


class Reward(db.Model):
    """Rewards"""
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'
