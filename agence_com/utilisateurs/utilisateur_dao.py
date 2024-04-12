import database as db
import flask_bcrypt as bcrypt
from utilisateurs.utilisateur import Utilisateur
#from utilisateur import Utilisateur

class UtilisateurDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, utl:Utilisateur):
       
        sql = "INSERT INTO utilisateurs (nom, username, mdp) VALUES (%s, %s, %s)"
        params = (utl.nom, utl.username, utl.mdp)
        try:
            UtilisateurDao.cursor.execute(sql,params)
            UtilisateurDao.connexion.commit()
            message = "Success"
        except Exception as exc:
            message = "Error"
        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM utilisateurs"
        UtilisateurDao.cursor.execute(sql)
        utilisateurs = UtilisateurDao.cursor.fetchall()
        
        return utilisateurs
    
    @classmethod
    def get_one(cls,username,mdp):
        sql = "SELECT * FROM utilisateurs WHERE username=%s"
        try:
            UtilisateurDao.cursor.execute(sql, (username,))
            utilisateur = UtilisateurDao.cursor.fetchone()
            if utilisateur:
                if bcrypt.check_password_hash(utilisateur[3], mdp):
                    message = "Success"
        except Exception as ex:
            message = "Error"
            utilisateur = []
        return (message,utilisateur)