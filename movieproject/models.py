from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from movieproject import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    gebruikersnaam = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    user_role = db.Column(db.String())

    def __init__(self, email, gebruikersnaam, password, role):
        self.email = email
        self.gebruikersnaam = gebruikersnaam
        self.password_hash = generate_password_hash(password)
        self.user_role = role
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
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