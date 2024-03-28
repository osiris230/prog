import database as db
from departement.departement import Departement

class DepartementDao:
    connexion = db.connect_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, id, nom, emplacement):
        sql = "INSERT INTO departement(id,nom,emplacement) VALUES (%s,%s,%s)"
        params = (id, nom, emplacement)
        DepartementDao.cursor.execute(sql,params)
        DepartementDao.connexion.commit()
        DepartementDao.cursor.close()
        print(f"Ajout du département avec l'id : {id}.")
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM departement"
        DepartementDao.cursor.execute(sql)
        Departements = DepartementDao.cursor.fetchall()
        DepartementDao.cursor.close()
        return Departements
    
    @classmethod
    def delete(cls,id):
        sql = "DELETE FROM departement WHERE id=%s"
        DepartementDao.cursor.execute(sql,(id,))
        DepartementDao.connexion.commit()
        DepartementDao.cursor.close()
        print(f"Suppression du département avec l'id : {id}.")
    
    @classmethod
    def update(cls,id,nom,emplacement):
        sql = "UPDATE departement SET nom=%s,emplacement=%s WHERE id=%s"
        params = (id, nom, emplacement)
        DepartementDao.cursor.execute(sql,params)
        DepartementDao.connexion.commit()
        DepartementDao.cursor.close()
        print(f"Mise à jour du département avec l'id : {id}.")