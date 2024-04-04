import database as db

def liste():
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    sql = "SELECT * FROM etudiant"
    cursor.execute(sql)
    resultats = cursor.fetchall()
    cursor.close()
    
    return resultats