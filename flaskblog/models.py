# Models Page

# Dependencies
from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, String, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    # Use as a string here because we will hash the image_files later
    image_file = Column(String(20), nullable=False, default="default.jpg")
    # Will be implementing hashing algorithm that will return 60 charater passwords
    password = Column(String(60), nullable=False)
    posts= relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}' )"

class Post(db.Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DATETIME, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}' )"