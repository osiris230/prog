from flask import Flask, render_template, url_for
import employe
import departement


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/employe")
def employes():
    employes = employe.liste()
    return render_template("employe.html", employes=employes)

@app.route("/add-employe")
def add_employe():
    return render_template("add_employe.html")

@app.route("/departements")
def departements():
    departements = departement.dliste()
    return render_template("departements.html", departements=departements)

@app.route("/add-departements")
def add_departements():
    return render_template("add_departements.html")