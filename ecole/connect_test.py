import mysql.connector as mysql

connection= mysql.connect(
    user='root',
    password= '',
    host='localhost',
    database='ecole'
)
print(connection)
request = connection.cursor()
request.execute("select * from etudiant")
result = request.fetchall()
print(result)
