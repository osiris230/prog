import mysql.connector as mysql

def connexion():
    return mysql.connect(
        user='root',
        host='localhost',
        password='',
        database='ecole'
    )