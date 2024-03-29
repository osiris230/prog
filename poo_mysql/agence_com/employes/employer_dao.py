#DAO = Data Access Object
import database as db
from employes.employe import Employe
class EmployeDao:
    connexion = db.connect_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls,emp:Employe):
        sql = "INSERT INTO employe(nom,prenom,matricule,fonction,departement) VALUES (%s,%s,%s,%s,%s)"
        params = (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.departement)
        try:
            EmployeDao.cursor.execute(sql,params)
            EmployeDao.connexion.commit()
            EmployeDao.cursor.close()
            message = f"Ajout de l'employé avec le matricule {emp.matricule}."
            
        except Exception:
            message = f"Une erreur est survenue lors de l'ajout, contactez Abdou si l'erreure persiste."
        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM employe"
        try:
            EmployeDao.cursor.execute(sql)
            employes = EmployeDao.cursor.fetchall()
            EmployeDao.cursor.close()
            message = "Success"
        except Exception:
            employes = []
            message = "Erreur lors de la récupération des donnés."
        return (employes, message)
    
    
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
    def update(cls,emp:Employe):
        sql = "UPDATE employe SET nom=%s,prenom=%s,matricule=%s,fonction=%s,departement=%s WHERE id=%s"
        params = (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.departement)
        EmployeDao.cursor.execute(sql,params)
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()
        print(f"Mise à jour de l'employé avec le matricule {emp.matricule}.")