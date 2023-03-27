#Imports
from flask import Flask, render_template, session, redirect, url_for, session
from forms import *
from flask_migrate import Migrate
from models import *

#App Configuration
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'accounts.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'MijnSecretKey'

db.init_app(app)

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
        email = form.email.data
        password = form.password.data
        
        user = Accounts.query.filter_by(email=email, password=password).first()
        
        if user:
            return redirect(url_for('Lijst'))

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