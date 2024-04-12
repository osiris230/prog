from flask import Flask, render_template, url_for, request, session, redirect
from flask_bcrypt import Bcrypt

from employes.Employe import Employe
from employes.employe_dao import EmployeDao
from departements.departement import Departement
from departements.departement_dao import DepartementDao
from utilisateurs.utilisateur import Utilisateur
from utilisateurs.utilisateur_dao import UtilisateurDao


app = Flask(__name__)
app.secret_key='secretkey'
bcrypt = Bcrypt(app) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    message=None
    utilisateur=None
    req = request.form
    if request.method == "POST":
        nom = req['nom']
        username = req['username']
        mdp = req['mdp']
        hashed_password = bcrypt.generate_password_hash(mdp).decode('utf-8')
        if nom=="" or username=="" or mdp=="":
            message="error"
        else:
                
            utilisateur = Utilisateur(nom,username,hashed_password)
            message = UtilisateurDao.create(utilisateur)
        #print(message)
    return render_template(f'register.html', message=message,utilisateur=utilisateur)


@app.route("/login", methods=["GET", "POST"])
def login():
    req= request.form
    message = None
    utilisateur = None
    if request.method == "POST":
        username = req['username']
        mdp = req['mdp']
        if username == '' or mdp == '':
            message = 'error'
        else:
            (message,utilisateur) =  UtilisateurDao.get_one(username,mdp)
            if message=='Success' and utilisateur != None:
                if bcrypt.check_password_hash(utilisateur[3], mdp):
                    session['username'] = utilisateur[2]
                    session['nom'] = utilisateur[1]
                    return redirect(url_for('home'))
                else:
                    message = 'Nom d\'utilisateur ou mot de passe incorrect.'
            else:
                message = 'Nom d\'utilisateur ou mot de passe incorrect.'
        print(message)
            
    return render_template("login.html",message=message,utilisateur=utilisateur)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/employe")
def employes():
    if 'username' not in session:
        return redirect(url_for('login'))
    employes = EmployeDao.get_all()
    return render_template("employe.html", employes=employes)

@app.route("/add-employe",methods=["POST","GET"])
def add_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message = None
    employe = None
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
    return render_template("add_employe.html",employe=employe,message=message)

@app.route("/departements")
def departements():
    departements = DepartementDao.list_all()
    return render_template("departements.html", departements=departements)

@app.route("/add-departements",methods=["POST","GET"])
def add_departements():
    req = request.form
    message = None
    departement = None
    if request.method == "POST":
        nom = req['nom']
        emplacement = req['emplacement']
        direction = req['direction']
        if nom=="" or emplacement=="" or direction=="":
            message="error"
        else:
            departement = Departement(nom,emplacement,direction)
            message = DepartementDao.create(departement)
    return render_template("add_departements.html",message=message,departement=departement)