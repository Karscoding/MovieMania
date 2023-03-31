#Imports
from flask import Flask, render_template, redirect, url_for, session, request, flash
from forms import *
from flask_migrate import Migrate
from models import *
from flask_login import login_user, login_required, logout_user, LoginManager

#App Configuration
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'MijnSecretKey'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

#Default Path
@app.route("/" ,methods=['GET', 'POST'])
def Main():
    return render_template('main.html')

#Lijst Path
@app.route("/Lijst")
@login_required
def Lijst():
    films = Films.query.order_by('titel')
    return render_template("Lijst.html", films=films)

#Login Path
@app.route("/Login" ,methods=['GET', 'POST'])
def Login():
    form = InlogForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
    if user.check_password(form.password.data) and user is not None:
        login_user(user)
        flash('Succesvol ingelogd.')
    next = request.args.get('next')
    if next == None or not next[0]=='/':
        next = url_for('Info')
        return redirect(next)
        
    return render_template("Login.html", form=form)

#Registratie Path
@app.route("/Registratie",methods=['GET', 'POST'])
def registratie():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Dank voor de registratie. Er kan nu ingelogd worden! ')
        
        
        return redirect(url_for('Login'))
    
    return render_template("Registratie.html", form=form)

#Info Path
@app.route("/Info")
def Info():
    return render_template("Informatie.html")

@app.route("/AddFilm",methods=['GET', 'POST'])
@login_required
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
@login_required
def DelFilm():
    form = DeleteForm()
    films = Films.query.all()
    
    if form.validate_on_submit():
        id = form.id.data
        cursor = Films.query.get(id)
        db.session.delete(cursor)
        db.session.commit()
        
        return redirect(url_for('Lijst'))
    return render_template("DelFilm.html", form=form, films=films)

#Run
if __name__=='__main__':
    app.run(debug=True)