import os
from flask_sqlalchemy import SQLAlchemy
from app import db
from flask_login import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login_manager.user_loader()
    def load_user(user_id):
        return User.query.get(user_id)


    
        
class Films(db.Model):
    
    __tablename__ = 'Films'
    id = db.Column(db.Integer,primary_key = True)
    titel = db.Column(db.Text)
    jaar = db.Column(db.Integer)
    genre = db.Column(db.Text)
    lengte = db.Column(db.Text)
    description = db.Column(db.Text)
    rating = db.Column(db.Integer)
    image = db.Column(db.Text)
    
    def __init__(self, titel, jaar, genre, lengte, description, rating, image):
        self.titel = titel
        self.jaar = jaar
        self.genre = genre
        self.lengte = lengte
        self.description = description
        self.rating = rating
        self.image = image