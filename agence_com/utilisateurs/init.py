from utilisateur_dao import UtilisateurDao

(message,utilisateur)= UtilisateurDao.get_one('Diallo123','123')

print(message,utilisateur)