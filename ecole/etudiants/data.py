"""
    - Ce fichier contient l'ensemble des fonctions d'un étudiant
    - Dans ce projet notre base de données sera des dictionnaires ou listes
"""
def add(nom, prenom, matricule, date_naissence):
    etudiants = {
        "nom" : nom, 
        "prenom" : prenom,
        "matricule" : matricule,
        "date_naissance" : date_naissence,
    }
    return etudiants


def get(etudiants, matricule):
    for k,v in etudiants.items():
        if matricule == v:
            print(f"{k} : {v}")
            break


def get_all(etudiants):
    print("liste des étudiants : ")
    print("--------------------------------------------------")
    for k,v in etudiants.items():
        print(f"{k} : {v}")
        print("--------------------------------------------------")
        