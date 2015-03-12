import mysql.connector.errors as Error

class Equipement:

	def __init__(self,database):
		self.database=database


	def createTableEquipement(self):
		'''
			Cree la table equipement
				numero - type integer, l'identifiant et la clef primaire d'un equipement
				nom - type text, le nom de l'equipement
				numeroInstallation - type integer, le numero de l'installation liee a la table
		'''	
		try:
			self.database.execute("CREATE TABLE equipement(numero integer ,nom text, numeroInstallation integer, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			print ("TABLE equipement : creation impossible car la table existe deja")


	def insertInTableEquipement(self, numero, nom, numeroInstallation):
		'''
			Insere un equipement 
				numero - type integer, l'identifiant et la clef primaire d'un equipement
				nom - type text, le nom de l'equipement
				numeroInstallation - type integer, le numero de l'installation liee a la table
		'''
		try:
			self.database.execute("INSERT INTO equipement (numero,nom,numeroInstallation) VALUES (%s,%s,%s)",(numero,nom,numeroInstallation))
		except Error.IntegrityError:
			print("TABLE equipement : impossible d'inserer l'equipement n° "+numero+" car elle est deja presente dans la table")

                                        
	def deleInTableEquipement(self,numero):
		try:
			self.database.execute("DELETE FROM equipement WHERE equipement.numero=(%s)",(numero,))
		except Exception:
			print("Ce numero n'existe pas")
                        

	def afficheEquipement(self):
		for row in self.database.execute('SELECT * FROM equipement ORDER BY nom'):
			print (row)


	# AJOUT DE LA CLEF ETRANGERE

	def addForeignKeyInstallation(self):
		'''
			Ajoute une clef etrangere 'FK_Installation' sur la table equipement
				numeroInstallation de la table equipement fait reference a la clef primaire numero de la table installation 
		'''
		try:
			self.database.execute("ALTER TABLE equipement ADD CONSTRAINT FK_Installation FOREIGN KEY  (numeroInstallation) REFERENCES installation(numero)")
		except Error.DatabaseError:
			print("TABLE equipement : impossible d'ajouter la clef etrangere 'FK_Installation' car elle existe deja")
		

	# DROP

	def dropForeignKeyInstallation(self):
		'''	
			Supprime la clef etrangere FK_Installation
		'''
		try:
			self.database.execute("ALTER TABLE equipement DROP FOREIGN KEY FK_Installation")
		except Error.DatabaseError:
			print("TABLE equipement : impossible de supprimer la clef etrangere 'FK_Installation' car elle n'existe pas")


	def dropTableEquipement(self):
		'''
			Supprime la table equipement
		'''
		try:
			self.database.execute("DROP TABLE IF EXISTS equipement")
		except Error.IntegrityError:
			print("TABLE equipements : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes")	
		