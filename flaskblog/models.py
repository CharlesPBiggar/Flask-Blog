# Models Page

# Dependencies
from datetime import datetime
from flaskblog import db
from sqlalchemy import Column, Float, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    # Use as a string here because we will hash the image_files later
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    # Will be implementing hashing algorithm that will return 60 charater passwords
    password = db.Column(db.String(60), nullable=False)
    posts= db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}' )"

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}' )"