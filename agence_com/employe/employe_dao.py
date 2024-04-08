import database as db
from employe.Employe import Employe

class EmployeDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employe"
        EmployeDao.cursor.execute(sql)
        try:
            employes = EmployeDao.cursor.fetchall()
            message = "Success"
        except Exception as err:
            employes = []
            message = "Error"
        return employes, message
    
    @classmethod
    def add(emp:Employe):
        sql = "INSERT INTO employe (nom, prenom, matricule, fonction, departement) VALUES (%s,%s,%s,%s,%s)"
        params = (emp.nom,emp.prenom,emp.matricule,emp.fonction,emp.departement)
        EmployeDao.cursor.execute(sql,params)
        EmployeDao.connexion.commit()