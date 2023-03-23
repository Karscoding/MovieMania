from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField)
from wtforms.validators import DataRequired

class InlogForm(FlaskForm):
    email = StringField('Voer je e-mail in', validators=[DataRequired()])
    password = StringField('Voer je wachtwoord in', validators=[DataRequired()])

    submit = SubmitField('Verzend')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MijnSecretKey'

@app.route("/" ,methods=['GET', 'POST'])
def root():
    return render_template('main.html')

@app.route("/Lijst")
def Lijst():
    return render_template("Lijst.html")

@app.route("/Login" ,methods=['GET', 'POST'])
def Login():
    form = InlogForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data

        return redirect(url_for("Info"))

    return render_template("Login.html", form=form)

@app.route("/Info")
def Info():
    return render_template("Informatie.html")

@app.route("/Registratie")
def registratie():
    return render_template("Registratie.html")




if __name__=='__main__':
    app.run(debug=True, port=3333)