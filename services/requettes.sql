Select inst.nomInstallation, inst.adresse, inst.code_postal from installations inst where ville = "cholet" and inst.numeroInstallation in(Select equip.numeroInstallation_activite from equipement equip, equipements_Assoc_activites equipActivite where equip.idEquipement=equipActivite.idEquipement_Activite and equipActivite.codeActivite in (select codeActivite from activite where libeleActivite="Vol à voile"))
Select i.nom, i.numero from installations i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on equip.numero=equipActivite.numero_equipement JOIN activite a on a.numeo=ea.numeo_activite where ville like '? 'and a.nom like '%?%'
Select i.nomInstallation, i.numeroInstallation from installations i JOIN equipement e on i.numeroInstallation=e.numeroInstallation_activite JOIN equipements_Assoc_activites ea on e.idEquipement=ea.idEquipement_Activite JOIN activite a on a.codeActivite=ea.codeActivite where i.ville= 'Nantes 'and a.libeleActivite like 'Saut'