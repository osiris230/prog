#DAO = Data Access Object
import database as db
from employes.employe import Employe
class EmployeDao:
    connexion = db.connect_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls,nom,prenom,matricule,fonction,departement):
        sql = "INSERT INTO employe(nom,prenom,matricule,fonction,departement) VALUES (%s,%s,%s,%s,%s)"
        params = (nom, prenom, matricule, fonction, departement)
        EmployeDao.cursor.execute(sql,params)
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()
        print(f"Ajout de l'employé avec le matricule {matricule}.")
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM employe"
        EmployeDao.cursor.execute(sql)
        employes = EmployeDao.cursor.fetchall()
        EmployeDao.cursor.close()
        return employes
    
    @classmethod
    def list_one(cls,matricule):
        sql = "SELECT * FROM employe WHERE matricule=%s"
        EmployeDao.cursor.execute(sql, (matricule,))
        employe = EmployeDao.cursor.fetchone()
        EmployeDao.cursor.close()
        return employe
    
    @classmethod
    def delete(cls,matricule):
        sql = "DELETE FROM employe WHERE matricule=%s"
        EmployeDao.cursor.execute(sql,(matricule,))
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()
        print(f"Suppression de l'employé avec le matricule {matricule}.")
    
    @classmethod
    def update(cls,nom,prenom,matricule,fonction,departement, id):
        sql = "UPDATE employe SET nom=%s,prenom=%s,matricule=%s,fonction=%s,departement=%s WHERE id=%s"
        params = (nom, prenom, matricule, fonction, departement, id)
        EmployeDao.cursor.execute(sql,params)
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()
        print(f"Mise à jour de l'employé avec le matricule {matricule}.")