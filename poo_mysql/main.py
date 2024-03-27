from Etudiant import Etudiant

code_permanent = input("Donnez le code permanent de l'étudiant : ")
nom = input("Donnez le nom de l'étudiant : ")
prenom = input("Donnez le prénom de l'étudiant : ")
date_naissance = input("Donnez la date de naissance de l'étudiant : ")
specialite = input("Donnez la spécialité de l'étudiant : ")
etu = Etudiant(code_permanent, nom, prenom, date_naissance, specialite)
#etu.create(code_permanent, nom, prenom, date_naissance, specialite)
etu.list()

#etu.delete()