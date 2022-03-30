from flask import current_app
from sqlalchemy.sql import func

from project import db

class Book(db.Model):
    """
    Book Model
    """

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return '<Book %r>' % self.title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
