class Departement:
    def __init__(self,id,nom,emplacement):
        self.__id = id
        self.__nom= nom
        self.__emplacement = emplacement

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def emplacement(self):
        return self.__emplacement

    @emplacement.setter
    def emplacement(self, value):
        self.__emplacement = value

