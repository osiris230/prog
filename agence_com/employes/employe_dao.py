import database as db
from employes.Employe import Employe

class EmployeDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employe"
        EmployeDao.cursor.execute(sql)
        employers = EmployeDao.cursor.fetchall()
        return employers
    
    @classmethod
    def add(cls,emp:Employe):
        sql = "INSERT INTO employe (nom, prenom, matricule, fonction, departement) VALUES (%s,%s,%s,%s,%s)"
        params = (emp.nom,emp.prenom,emp.matricule,emp.fonction,emp.departement)
        try:
            EmployeDao.cursor.execute(sql,params)
            EmployeDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            message = "Error"
        return message
    
    @classmethod
    def get_one(cls,matricule):
        sql = "SELECT * FROM employe WHERE matricule=%s"
        try:
            EmployeDao.cursor.execute(sql, (matricule,))
            message = "Success"
            employe = EmployeDao.cursor.fetchone()
        except Exception as ex:
            message = "Erreur lors de la recherche"
            employe = []
        return (message,employe)