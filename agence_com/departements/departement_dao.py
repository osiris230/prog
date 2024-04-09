import database as db
from departements.departement import Departement

class DepartementDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, dpt:Departement):
        sql = "INSERT INTO departement(nom,emplacement,direction) VALUES (%s,%s,%s)"
        params = (dpt.nom, dpt.emplacement, dpt.direction)
        try:
            DepartementDao.cursor.execute(sql,params)
            DepartementDao.connexion.commit()
            
            message = f"Ajout du département : {dpt.nom}."
        except Exception as exc:
            message = exc
            if 'Duplicate entry' in exc:
                message = f"Le département '{dpt.nom}' existe déjà."

        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM departement"
        DepartementDao.cursor.execute(sql)
        Departements = DepartementDao.cursor.fetchall()
        
        return Departements
    
    @classmethod
    def delete(cls,id):
        sql = "DELETE FROM departement WHERE id=%s"
        DepartementDao.cursor.execute(sql,(id,))
        DepartementDao.connexion.commit()
        
        print(f"Suppression du département avec l'id : {id}.")
    
    @classmethod
    def update(cls,id, dpt:Departement):
        sql = "UPDATE departement SET nom=%s,emplacement=%s WHERE id=%s"
        params = (id,dpt.nom, dpt.emplacement, dpt.direction)
        DepartementDao.cursor.execute(sql,params)
        DepartementDao.connexion.commit()
        
        print(f"Mise à jour du département : {dpt.nom}.")