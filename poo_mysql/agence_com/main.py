from employes.employer_dao import EmployeDao
from employes.employe import Employe
from departement.departement_dao import DepartementDao
from departement.departement import Departement


#emp = Employe("Bobby","Bob","BB5678","Web","IT")
#data = EmployeDao.create(emp)
#print(data)
employes,message = EmployeDao.list_all()
print(employes,message)


#dpt = Departement("IT","étage 2","John")
#DepartementDao.create(dpt)