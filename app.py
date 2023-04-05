from movieproject import app, db
from flask import  render_template, redirect, url_for, session, request, flash
from flask_login import login_user, login_required
from movieproject.models import Films, User
from movieproject.forms import InlogForm, RegistrationForm, FilmForm, DeleteForm


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
    
        if user is not None and user.check_password(form.password.data) :
            login_user(user)
            flash('Succesvol ingelogd.')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('Main')
                return redirect(next)
        
    else:
        print("faal if 1")

    

        
    return render_template("Login.html", form=form)

#Registratie Path
@app.route("/Registratie",methods=['GET', 'POST'])
def registratie():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.submit():
            print('IT WORKS OMG')
            user = User(form.email.data,
                        form.name.data,
                        form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("account aangemaakt")
            return redirect(url_for('Login'))
        
    return render_template('Registratie.html', form=form)

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