from utils import *
from db_init import *
from classement import afficherClassement

nbMaxEquipier = 3

def jeu():
    personnages = chargerPersonnages()
    pseudo = recupererChoixTextuel("Veuillez choisir un pseudo", afficherMessageStringInvalide)
    equipe = creerEquipe(personnages)
    combat(equipe, pseudo)

#Combat
def combat(equipe, pseudo):
    vague = 1
    equipeEnVie = [*equipe]
    while True:
        monstre = genererMonstreAleatoire()
        victoire = lancer_vague(equipeEnVie,monstre)
        if not victoire:
            score = {"id" : 1,  "player_name" : pseudo, "waves" : vague}
            insererScore(score)
            afficherMessageFinPartie(vague)
            afficherClassement()
            return
        vague += 1
        print(f"Vous avez battu le monstre {monstre.name}")

def lancer_vague(equipeEnVie, monstre):
        while monstreIsAlive(monstre):
            for personnage in equipeEnVie:
                attaquer(personnage, monstre)
                if(not monstreIsAlive(monstre)):
                    return True
            attaqueDuMonstre(equipeEnVie, monstre)
            if not teamIsAlive(equipeEnVie):
                return False

def isAlive(personnage):
    return personnage.hp > 0

def teamIsAlive(equipe):
    nbMort = 0
    for p in equipe:
        if(not isAlive(p)):
            nbMort +=1
    return nbMort != len(equipe)

def monstreIsAlive(monstre):
    return monstre.hp > 0

def attaquer(personnage, monstre):
    monstre.hp -= (personnage.attack - monstre.defense) 

def attaqueDuMonstre(equipeEnVie, monstre):
    indexAleatoire = getNombreAleatoire(len(equipeEnVie))
    personnageCible = equipeEnVie[indexAleatoire-1]
    personnageCible.hp -= (monstre.attack - personnageCible.defense)
    if(not isAlive(personnageCible)):
        equipeEnVie.remove(personnageCible)

#Gestion équipe
def creerEquipe(personnages):
    equipe = []
    personnagesDisponibles = personnages
    while (len(equipe) < nbMaxEquipier): 
        messageSelection = formerMessageSelection(personnagesDisponibles)
        choixUtilisateur = recupererChoixNumerique(messageSelection, personnagesDisponibles, afficherMessageEntierInvalide)
        ajouterEquipier(personnagesDisponibles, choixUtilisateur, equipe)
    return equipe

def estDejaDansListe(personnage, equipe):
    for p in equipe:
        if (personnage.id == p.id):
            return True
    return False

def ajouterEquipier(personnagesDisponibles, choixUtilisateur, equipe):
    equipier = personnagesDisponibles[choixUtilisateur-1]
    equipe.append(equipier)
    personnagesDisponibles.remove(equipier)
    print(f"personnage {equipier.name} ajoute")
