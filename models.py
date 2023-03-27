import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Accounts(db.Model):
    
    __tablename__ = 'Accounts'
    id = db.Column(db.Integer,primary_key = True)
    gebruikersnaam = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    
    def __init__(self, name, email, password):
        self.gebruikersnaam = name
        self.email = email
        self.password = password
        
    def __repr__(self):
        return f"Gebruikersnaam: {self.gebruikersnaam} Email: {self.email} Wachtwoord: {self.password}"
    
if __name__ == '__main__':
        db.create_all()