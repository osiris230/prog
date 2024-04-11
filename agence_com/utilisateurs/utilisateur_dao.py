import database as db
from utilisateurs.utilisateurs import Utilisateur

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
        sql = "SELECT * FROM utilisateurs WHERE username=%s AND mdp=%s"
        try:
            UtilisateurDao.cursor.execute(sql, (username,mdp))
            utilisateur = UtilisateurDao.cursor.fetchone()
            message = "Success"
        except Exception as ex:
            message = "Error"
            utilisateur = []
        return (message,utilisateur)