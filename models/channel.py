"""
Channel Class
"""

from sqlalchemy import Column, Integer, String

from app import db


class Channel(db.Model):
    """Channels"""
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'
