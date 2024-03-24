"""
    - Ce fichier contient l'ensemble des fonctions d'un admin
    - Dans ce projet notre base de données sera des dictionnaires ou listes
"""
def add(nom, prenom, matricule, date_naissence):
    admin = {
        "nom" : nom, 
        "prenom" : prenom,
        "matricule" : matricule,
        "date_naissance" : date_naissence,
    }
    return admin


def get(admin, matricule):
    for k,v in admin.items():
        if matricule == v:
            print(f"{k} : {v}")
            break


def get_all(admin):
    print("liste des admins : ")
    print("--------------------------------------------------")
    for k,v in admin.items():
        print(f"{k} : {v}")
        print("--------------------------------------------------")
        