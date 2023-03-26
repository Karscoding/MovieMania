#Imports
import os
from flask import Flask, render_template, session, redirect, url_for, session
from forms import *
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#App Configuration
app = Flask(__name__)

app.config['SECRET_KEY'] = 'MijnSecretKey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'accounts.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Accounts(db.Model):
    
    __tablename__ = 'Accounts'
    id = db.Column(db.Integer,primary_key = True)
    gebruikersnaam = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    
    def __init__(self, name, email, password):
        self.gebruikersnaam = name
        self.email = email
        self.password = password
        db.create_all()
        
    def __repr__(self):
        return f"Gebruikersnaam: {self.gebruikersnaam} Email: {self.email} Wachtwoord: {self.password}"

#Default Path
@app.route("/" ,methods=['GET', 'POST'])
def Main():
    return render_template('main.html')

#Lijst Path
@app.route("/Lijst")
def Lijst():
    return render_template("Lijst.html")

#Login Path
@app.route("/Login" ,methods=['GET', 'POST'])
def Login():
    form = InlogForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data

        return redirect(url_for("Info"))

    return render_template("Login.html", form=form)

#Registratie Path
@app.route("/Registratie",methods=['GET', 'POST'])
def registratie():
    form = RegistratieForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        user = Accounts.query.filter_by(email=email).first()
        
        if user:
            return redirect(url_for('registratie'))
        
        NewAccount = Accounts(name,email,password)
        db.session.add(NewAccount)
        db.session.commit()
        
        return redirect(url_for('Info'))
    
    return render_template("Registratie.html", form=form)

#Info Path
@app.route("/Info")
def Info():
    accounts = Accounts.query.all()
    return render_template("Informatie.html", accounts=accounts)

#Run
if __name__=='__main__':
    app.run(debug=True)