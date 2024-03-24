"""
    - Ce fichier sert de programme principale.
    - Dans ce fichier on va faire appel a nos différent modulespi packages.
    - C'est le point d'entrer de notre application ou projet.
"""
# Importation
import etudiants.data #as da
import etudiants.notes as student_rate
from etudiants import (data as data_etu, notes as notes_etu)
from enseignants import data as data_ens

etudiant = data_etu.add("Labrie", "Stéphane", "LS5634", "1986-12-13")
data_etu.get_all(etudiant)

etu = etudiants.data.add()
student_rate
