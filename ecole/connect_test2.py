import mysql.connector as mysql

connection= mysql.connect(
    user='root',
    password= '',
    host='localhost',
    database='ecole'
)

cursor = connection.cursor()

def insertion():
    sql_insert_query = "INSERT INTO eleves (code_permanent, nom, prenom, date_naissance,spécialite) VALUES ('J12345', 'Rambo', 'John', '1965-01-01', 'guerre')"
    