from Etudiant import Etudiant

def menu():
    while True:
        print("\nMenu:")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Mettre à jour un étudiant")
        print("4. Supprimer un étudiant")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-5): ")

        if choix == '1':
            code_permanent = input("Donnez le code permanent de l'étudiant : ")
            nom = input("Donnez le nom de l'étudiant : ")
            prenom = input("Donnez le prénom de l'étudiant : ")
            date_naissance = input("Donnez la date de naissance de l'étudiant : ")
            specialite = input("Donnez la spécialité de l'étudiant : ")
            Etudiant.create(code_permanent, nom, prenom, date_naissance, specialite)
        elif choix == '2':
            Etudiant.list(Etudiant)
        elif choix == '3':
            code_permanent = input("Entrez le code permanent de l'étudiant à mettre à jour : ")
            nom = input("Entrez le nouveau nom : ")
            prenom = input("Entrez le nouveau prénom : ")
            specialite = input("Entrez la nouvelle spécialité : ")
            Etudiant.update(code_permanent, nom, prenom, specialite)
        elif choix == '4':
            code_permanent = input("Entrez le code permanent de l'utilisateur à supprimer : ")
            Etudiant.delete(code_permanent)
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")