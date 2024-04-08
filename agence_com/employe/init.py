from employe_dao import EmployeDao

(message, employes) = EmployeDao.get_all()
print(message,employes)