from bottle import route, run, request, response
import sys
sys.path.append("../model")
from dao import Dao
from installation import Installation
from equipement import Equipement
from activite import Activite
import json

def toInstallations(argument):
    '''
        fonction qui transforme une installation de la base de données en objet Installation
    '''
    # instanciation de l'objet Installation
    objectInstallation = Installation(argument[0],argument[1],argument[2],argument[3],argument[4],argument[5],argument[6],argument[7])
    
    # connexion
    dao = Dao()
    #dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    # on récupère toutes les lignes de la table équipement
    cur = dao.getCursor()
    cur.execute("Select * from equipement where numeroInstallation = %s ",(argument[0],))
    rows = cur.fetchall()

    # création de l'objet 
    listObjectEquipement = list(map(toEquipement, rows))
    for obj in listObjectEquipement:
        objectInstallation.addEquipement(obj)
    return objectInstallation

def toEquipement(argument):
    equipement = Equipement(argument[0],argument[1],argument[2])

    # connexion
    dao = Dao()
    #dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    # on récupère le numéro d'activité de l'équipement
    cur = dao.getCursor()
    rows = cur.execute("Select numeroActivite from equipements_Assoc_activites where numeroEquipement = %s ",(argument[0],))
    rows = cur.fetchall()

    # création de l'object
    listObjectActivite = list(map(getActivite,rows))
    activite = list(map(toActivite, listActivite))
    for activite in activite:
        equipement.addActivite(activite)
    return equipement

def toActivite(argument):
    activite = Activite(argument[0],argument[1],argument[2])
    return activite


def getActivite(argument):
    dao = Dao()
    #dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = dao.getCursor()
    cur.execute("Select * from activite where numero = %s ",(argument[0],))
    row = cur.fetchone()
    return row



def todic(installation):
    listEquipement = []
    listActivite = []
    for equipement in installation.equipement:
        for activite in equipement.activite:
            listActivite.append(activite.__dict__)
        dictEquipement = equipement.__dict__
        dictEquipement['activite']=listActivite
        listEquipement.append(dictEquipement)
    inst=installation.__dict__
    inst['equipement']=listEquipement
    return inst

def installation(activite, ville):
    dao = Dao()
    #dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = dao.getCursor()
    cur.execute("Select  i.numero, i.nom, i.voie, i.adresse, i.codePostal, i.ville,  i.latitude, i.longitude from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
    rows = cur.fetchall()
    # Pour éviter les doublons
    rowsbis = list(set(rows))
    installation = list(map(toInstallations, rowsbis))

    #print (installation)
    return installation

@route('/installation')
def recherche():
    # Récuperation des argument passé en paramètre dans l'url
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)
    items = installation(activite,ville)
    myDictionary = (list(map(todic,items)))
    #print (myDictionary)
    return {'installations' : myDictionary}

@route('/ville')
def recherche():
    resultat=[]
    myDataBase=Dao()
    #myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = myDataBase.getCursor()
    cur.execute("Select ville from installation")
    rows = cur.fetchall()
    for membre in rows:
        sort={}
        sort['ville']=(membre[0])
        resultat.append(sort)
    #print(resultat)
    return json.dumps(resultat)
