from flask import Flask, render_template
import etudiant


app = Flask(__name__)

@app.route("/")
def home():
    titre = "Collège Cumberland"
    nom  = "Maxime St-Pierre"

    return render_template("index.html", titre=titre, nom=nom)

@app.route("/about")
def about():
    description = """
                    Cumberland College aims to provide its students with cutting-edge, up-to-date career training for success in today’s digital world. With campuses located in Montreal and Surrey, our college serves as the perfect destination for ambitious professionals seeking to launch a variety of digital marketing careers.
Born out of our desire to share our professional experiences and network of active industry experts, Cumberland College aims to provide aspiring digital marketing professionals with career-ready training. Our unique curriculum, designed by real, working digital marketing professionals, reflects the realities of what students need to know in this ever-changing industry. Combined with a practical learning approach, our courses equip students with invaluable tools and skill sets, preparing them for success as they launch their new careers in the field.
                  """
    return render_template("about.html", desc=description)

@app.route("/test")
def test():
    age = 32
    nom = "Maxime St-Pierre"
   
    
    etudiants = [
         {"nom":"St-Pierre","prenom":"Maxime","age":32},
         {"nom":"Labrie","prenom":"Stéphane","age":38},
         {"nom":"Motin-Ye","prenom":"Armel Joel","age":40},
         {"nom":"Eyong","prenom":"Bijou","age":36}
         
    ]
    return render_template("test.html", 
                           age=age, 
                           nom=nom,
                           etudiants=etudiants
                           )


@app.route("/test2")
def liste():
    etudiants = etudiant.liste()

    return render_template("test2.html",etudiants=etudiants)