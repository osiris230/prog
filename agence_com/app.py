from flask import Flask, render_template, url_for, request

from employes.Employe import Employe
from employes.employe_dao import EmployeDao
from departements.departement import Departement
from departements.departement_dao import DepartementDao


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
    employes = EmployeDao.get_all()
    return render_template("employe.html", employes=employes)

@app.route("/add-employe",methods=["POST","GET"])
def add_employe():
    req = request.form
    message = None
    if request.method == "POST":
        nom = req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        departement = req['departement']
        
        if nom=="" or prenom=="" or matricule=="" or fonction=="" or departement=="":
            message="error"
        else:
            employe = Employe(nom,prenom,matricule,fonction,departement)
            message = EmployeDao.add(employe)
        #print(message)
    return render_template("add_employe.html",message=message)

@app.route("/departements")
def departements():
    departements = DepartementDao.list_all()
    return render_template("departements.html", departements=departements)

@app.route("/add-departements")
def add_departements():
    return render_template("add_departements.html")

@app.route("/traitement", methods=['POST','GET'])
def traitement():
    return "add employe"