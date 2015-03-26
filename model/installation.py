
class Installation:
	def __init__(self, numero, nom, adresse, codePostal, ville, latitude, longitude):
		self.numero = numero
		self.nom = nom.decode()
		self.adresse = adresse.decode()
		self.codePostal = codePostal
		self.ville = ville.decode()
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
	 	return "{} - {} - {} - {} - {} - {} - {}".format(self.numero, self.nom, self.adresse, self.codePostal, self.ville, self.latitude, self.longitude)	