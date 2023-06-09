from movieproject import app, db
from flask import render_template, redirect, url_for, session, request, flash
from flask_login import login_user,logout_user, login_required, current_user
from movieproject.models import *
from movieproject.forms import InlogForm, RegistrationForm, FilmForm, DeleteForm


#Default Path
@app.route("/" ,methods=['GET', 'POST'])
def Main():
    return render_template('main.html')

#Lijst Path
@app.route("/Lijst")
@login_required
def Lijst():
    user = User.query.filter_by(id=current_user.id).first()
    userPerms = user.user_role
    userName = user.gebruikersnaam
    films = Films.query.order_by('titel')
    return render_template("Lijst.html", films=films, userPerms=userPerms, userName=userName)

#Login Path
@app.route("/Login" ,methods=['GET', 'POST'])
def Login():
    form = InlogForm()
    error = False
    try:
        user = User.query.filter_by(id=current_user.id).first()
        userName = user.gebruikersnaam
    except:
        userName = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
        
            if user is not None and user.check_password(form.password.data) :
                login_user(user)            
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('Main')
                    return redirect(next)
        error = True
                        
    return render_template("Login.html", form=form, error=error, userName=userName)

#Registratie Path
@app.route("/Registratie",methods=['GET', 'POST'])
def registratie():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.submit():
            user = User(form.email.data,
                        form.name.data,
                        form.password.data,
                        'User')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('Login'))
        
    return render_template('Registratie.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Main'))

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