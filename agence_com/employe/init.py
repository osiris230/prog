from employe_dao import EmployeDao
from Employe import Employe

#(message, employes) = EmployeDao.get_all()
#print(message,employes)

#employe = Employe("Diallo","Abdou","ABD12345","web","IT")
#message = EmployeDao.add(employe)
#print(message)

(message,employe) = EmployeDao.get_one("MP56897")
print((message,employe))