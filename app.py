from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('main.html')

@app.route("/Lijst")
def Lijst():
    return render_template("Lijst.html")

if __name__=='__main__':
    app.run(debug=True, port=3333)