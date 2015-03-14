
import mysql.connector.errors as Error


class Equipements_activites:

	def __init__(self,database):
		self.database=database

	def createTableEquipements_Assoc_activites(self):
		'''
			Cree la table equipements_Assoc_activites, la table association entre les tables equipement et activite
				numeroActivite - type integer, l'identifiant et la clef primaire de la table activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilisé par une activite
		'''
		try:
			self.database.execute("CREATE TABLE equipements_Assoc_activites(numeroActivite integer NOT NULL, numeroEquipement integer NOT NULL)")
		except Error.ProgrammingError:
			print ("TABLE equipements_Assoc_activites : creation impossible car la table existe deja")


	def insertInTableEquipements_Assoc_activites(self, numeroActivite, numeroEquipement):
		'''
			Insere une ligne dans la table equipements_Assoc_activites
				numeroActivite - type integer, l'identifiant et la clef primaire de la table activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilisé par une activite
		'''
		try:
			self.database.execute("INSERT INTO equipements_Assoc_activites (numeroActivite, numeroEquipement) VALUES (%s,%s)",(numeroActivite,numeroEquipement))
		except Error.IntegrityError:
			print("TABLE equipements_Assoc_activites : impossible s'inserer la ligne numeroActivite="+numeroActivite+" et numeroEquipement="+numeroEquipement+"car elle est deja presente dans la table")


	def deleInTableEquipements_Assoc_activites(self,numeroActivite):
		try:
			self.database.execute("DELETE FROM equipements_Assoc_activites WHERE equipements_activites.numeroActivite=(%s)",(numeroActivite,))
		except Exception:
			print("Ce numeroActivite n'existe pas")

	
	# AJOUT DES CLEFS ETRANGERES

	def addForeignKeyEquipement(self):
		'''
			Ajoute une clef etrangere 'FK_Equipement' sur la table equipements_activites
				numeroEquipement de la table equipements_activites fait reference a la clef primaire 'numero' de la table equipement 
		'''
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT FK_Equipement FOREIGN KEY (numeroEquipement) REFERENCES equipement(numero)")
		except Error.DatabaseError:
			print("TABLE equipements_activites : impossible d'ajouter la clef etrangere 'FK_Equipement' car elle existe deja")


	def addForeignKeyActivite(self):
		'''
			Ajoute une clef etrangere 'FK_Activite' sur la table equipements_activites
				numeroActivite de la table equipements_activites fait reference a la clef primaire 'numero' de la table activite 
		'''
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT FK_Activite FOREIGN KEY (numeroActivite) REFERENCES activite(numero)")
		except Error.DatabaseError:
			print("TABLE equipements_activites : impossible d'ajouter la clef etrangere 'FK_Activite' car elle existe deja")


	# DROP
			
	def dropForeignKeyEquipement(self):
		'''
			Supprime la clef etrangere 'FK_Equipement'
		'''
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY FK_Equipement")
		except Error.DatabaseError:
			print("TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Equipement' car elle n'existe pas")


	def dropForeignKeyActivite(self):
		'''
			Supprime la clef etrangere 'FK_Activite'
		'''
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY FK_Activite")
		except Error.DatabaseError:
			print("TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Activite' car elle n'existe pas")	


	def dropTableEquipements_Assoc_activites(self):
		'''
			Supprime la table equipements_Assoc_activites
		'''
		try:
			self.database.execute("DROP TABLE IF EXISTS equipements_Assoc_activites")
		except Error.IntegrityError:
			print("TABLE equipements_Assoc_activites : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes")		
	
