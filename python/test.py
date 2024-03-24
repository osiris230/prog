"""
Écrivez une fonction appelée tri_croissant qui prend une liste de nombres
en entrée et renvoie une nouvelle liste contenant les mêmes éléments triés
par ordre croissant.
"""
def creer_liste ():
    liste = []
    # control de saisir pour la taille de la liste 
    print("Entrez vos nombres. Tapez 'q' pour terminer.")
    while True:
        element = input("Entrez le prochain nombre (ou 'q' pour quitter): ")
        if element.lower() == 'q':
            break
        try:
            nombre = int(element)
            liste.append(nombre)
        except ValueError:
            print("Veuillez entrer un nombre valide ou 'q' pour terminer.")
    return liste
  
def tri_croissant(liste:list):
    return sorted(liste)

liste = creer_liste()
liste_trie = tri_croissant(liste)
print(liste_trie)  
