from decimal import *

class Installation :


	def __init__(self,database):
		self.database=database


	def createTableInstallation(self):
		try:
			self.database.execute("CREATE TABLE installations(numeroInstallation integer ,nomInstallation text, adresse text, code_postal integer, ville text, latitude float ,longitude float, PRIMARY KEY (numeroInstallation))")
		except Exception:
			#IOError
			#ValueError
			print ("La table existe déjà")



	def insertInTableInstallation(self,numeroInstallation,nomInstallation,adresse,code_postal,ville,latitude,longitude):
		try:
			self.database.execute("INSERT INTO installations (numeroInstallation,nomInstallation,adresse,code_postal,ville,latitude,longitude) VALUES (%s,%s,%s,%s,%s,%s,%s)",(numeroInstallation,nomInstallation,adresse,code_postal,ville,latitude,longitude))
		except Exception:
			print("Vous ne pouvez pas rentrer deux numeroInstallation identique")


                        
	def dropTableInstallation(self):
		self.database.execute("DROP TABLE IF EXISTS installations")

	def deleInTableInstallation(self,numeroInstallation):
                try:
                        delf.database.execute("DELETE FROM installations WHERE installations.numeroInstallation=(%s)",(numeroInstallation,))
                except Exception:
                        print("Ce numeroInstallation n'existe pas")

                        

	def afficheInstallation(self):
		for row in self.database.execute('SELECT * FROM installations ORDER BY nomInstallation'):
			print (row)


	def modiffierTableInstallation(self,numeroInstallation,nomInstallation,adresse,code_postal,ville,latitude,longitude):
		try:
			self.database.execute("UPDATE installations SET numeroInstallation=%s , nomInstallation=%s, adresse=%s ,code_postal=%s ,ville=%s ,latitude=%s ,longitude=%s  WHERE numeroInstallation = installations.numeroInstallation",(numeroInstallation,nomInstallation,adresse,code_postal,ville,latitude,longitude))
		except Exception:
			print("le numeroInstallation n'existe pas")