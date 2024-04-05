import database as db

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