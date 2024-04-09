import mysql.connector as mysql

def connexion_db():
    return mysql.connect(
        user='root',
        password= '',
        host='localhost',
        database='agence'
        )