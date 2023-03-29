import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Accounts(db.Model):
    
    __tablename__ = 'Accounts'
    id = db.Column(db.Integer,primary_key = True)
    gebruikersnaam = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    role = db.Column(db.Text)
    
    def __init__(self, name, email, password, role):
        self.gebruikersnaam = name
        self.email = email
        self.password = password
        self.role = role
        
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