from decimal import *
import mysql.connector.errors as Error

class Installation :


	def __init__(self,database):
		self.database=database


	def createTableInstallation(self):
		'''
			Cree la table installation
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'installation
				adresse - type text, l'adresse de l'installation
				codePostal - type integer, le code postal de l'installation
				ville - type text, la ville de l'installation
				latitude - type float, la latitude de la position de l'installation
				longitude - type float, la longitude de la position de l'installation
		'''
		try:
			self.database.execute("CREATE TABLE installation(numero integer ,nom text, adresse text, codePostal integer, ville text, latitude float ,longitude float, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			print ("TABLE installation : creation impossible car la table existe deja")


	def insertInTableInstallation(self, numero, nom, adresse, codePostal, ville, latitude, longitude):
		'''
			Insere une installation
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'installation
				adresse - type text, l'adresse de l'installation
				codePostal - type integer, le code postal de l'installation
				ville - type text, la ville de l'installation
				latitude - type float, la latitude de la position de l'installation
				longitude - type float, la longitude de la position de l'installation
		'''
		try:
			self.database.execute("INSERT INTO installation (numero, nom, adresse, codePostal, ville, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s)",(numero,nom,adresse,codePostal,ville,latitude,longitude))
		except Error.IntegrityError:
			print("TABLE installation : impossible d'inserer l'installation n° "+numero+" car elle est deja presente dans la table")

                        
	def deleInTableInstallation(self,numero):
		try:
			delf.database.execute("DELETE FROM installation WHERE installation.numero=(%s)",(numero,))
		except Exception:
			print("Ce numero n'existe pas")
   

	def afficheInstallation(self):
		for row in self.database.execute('SELECT * FROM installations ORDER BY nom'):
			print (row)


	def modiffierTableInstallation(self,numero,nom,adresse,code_postal,ville,latitude,longitude):
		try:
			self.database.execute("UPDATE installations SET numero=%s , nom=%s, adresse=%s ,code_postal=%s ,ville=%s ,latitude=%s ,longitude=%s  WHERE numero = installations.numero",(numero,nom,adresse,code_postal,ville,latitude,longitude))
		except Exception:
			print("le numero n'existe pas")


	def dropTableInstallation(self):
		'''
			Supprime la table installation
		'''
		try:
			self.database.execute("DROP TABLE IF EXISTS installation")
		except Error.IntegrityError:
			print("TABLE installations : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes")		