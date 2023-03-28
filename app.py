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
    films = Films.query.all()
    
    return render_template("Lijst.html", films=films)

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
    return render_template("Informatie.html")

@app.route("/AddFilm",methods=['GET', 'POST'])
def AddFilm():
    form = FilmForm()
    if form.validate_on_submit():
        titel = form.Titel.data
        jaar = form.Jaar.data
        genre = form.Genre.data
        lengte = form.Lengte.data
        desc = form.Description.data
        rating = form.Rating.data
        img = form.Imglink.data
        
        NewFilm = Films(titel,jaar,genre,lengte,desc,rating,img)
        db.session.add(NewFilm)
        db.session.commit()
        
        return redirect(url_for('Lijst'))
    
    return render_template("AddFilm.html", form=form)

@app.route("/DelFilm",methods=['GET', 'POST'])
def DelFilm():
    form = DeleteForm()
    
    if form.validate_on_submit():
        id = form.id.data
        cursor = Films.query.get(id)
        db.session.delete(cursor)
        db.session.commit()
        
        return redirect(url_for('Lijst'))
    return render_template("DelFilm.html", form=form)

#Run
if __name__=='__main__':
    app.run(debug=True)