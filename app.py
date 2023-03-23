from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('main.html')

@app.route("/Lijst")
def Lijst():
    return render_template("Lijst.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Info")
def Info():
    return render_template("Informatie.html")

@app.route("/Registratie")
def registratie():
    return render_template("Registratie.html")




if __name__=='__main__':
    app.run(debug=True, port=3333)