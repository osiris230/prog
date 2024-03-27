import connexion_db as db
class Etudiant:
    connexion = db.connexion()
    cursor = connexion.cursor()

    def __init__(self,code_permanent, nom, prenom, date_naissance, specialite):
        self.__code_permanent = code_permanent
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__specialite= specialite
        
    @property
    def code_permanent(self):
        return self.__code_permanent

    @code_permanent.setter
    def code_permanent(self, value):
        self.__code_permanent = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def date_naissance(self):
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        self.__date_naissance = value

    @property
    def specialite(self):
        return self.__specialite

    @specialite.setter
    def specialite(self, value):
        self.__specialite = value

    #CRUD
    def create(self,code_permanent, nom, prenom, date_naissance, specialite):
        sql = "INSERT INTO etudiant(code_permanent, nom, prenom, date_naissance, specialite) VALUES(%s,%s,%s,%s,%s)"
        params= (code_permanent,nom,prenom,date_naissance,specialite)
        Etudiant.cursor.execute(sql,params)
        Etudiant.connexion.commit()

    def list(self):
        sql = "SELECT * FROM etudiant"
        Etudiant.cursor.execute(sql)
        #etudiants = Etudiant.cursor.fetchall()
        print("--------------------------------")
        for code_permanent, nom, prenom, date_naissance, specialite in Etudiant.cursor:
            print(f"Code Permanent : {code_permanent}, \nNom : {nom}, \nPrénom : {prenom}, \nDate de Naissance : {date_naissance}, \nSpécialité : {specialite}")
            print("--------------------------------")

    def delete(self, code_permanent):
        sql = "DELETE FROM etudiant WHERE code_permanent=%s"
        Etudiant.cursor.execute(sql, (code_permanent,))
        Etudiant.connexion.commit()