from employes.employer_dao import EmployeDao
from employes.employe import Employe
from departement.departement_dao import DepartementDao
from departement.departement import Departement


#emp = Employe("Bobby","Bob","BB5678","Web","IT")
#data = EmployeDao.create(emp)
#print(data)
employes,message = EmployeDao.list_all()

for employe in employes:
    print(f"Nom : {employe[0]}, Prénom : {employe[1]}, Matricule : {employe[2]}, Fonction : {employe[3]}, Département : {employe[4]}")
    print("-----------------------------------------------------------------------------------")

#dpt = Departement("IT","étage 2","John")
#DepartementDao.create(dpt)