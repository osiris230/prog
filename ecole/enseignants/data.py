"""
    - Ce fichier contient l'ensemble des fonctions d'un enseignants    
    - Dans ce projet notre base de données sera des dictionnaires ou listes
"""
def add(nom, prenom, matricule, date_naissence):
    enseignants = {
        "nom" : nom, 
        "prenom" : prenom,
        "matricule" : matricule,
        "date_naissance" : date_naissence,
    }
    return enseignants


def get(enseignants, matricule):
    for k,v in enseignants.items():
        if matricule == v:
            print(f"{k} : {v}")
            break


def get_all(enseignants):
    print("liste des enseignants : ")
    print("--------------------------------------------------")
    for k,v in enseignants.items():
        print(f"{k} : {v}")
        print("--------------------------------------------------")
        