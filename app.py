#Imports
from flask import Flask, render_template, session, redirect, url_for, session
from forms import *

#App Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MijnSecretKey'

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
@app.route("/Registratie")
def registratie():
    form = RegistratieForm()
    return render_template("Registratie.html", form=form)

#Info Path
@app.route("/Info")
def Info():
    return render_template("Informatie.html")

#Run
if __name__=='__main__':
    app.run(debug=True)