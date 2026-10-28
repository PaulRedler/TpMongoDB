import sys
from utils import *
from db_init import * 
"""
choixMenu = ["Démarrer le jeu", "Afficher le classement", "Quitter"]

isEmptyOrWhiteSpace(chaine):
    retourne si la chaine est vide ou ne contient que des espaces

isInRange(tableauChoix,valeur):
    retourne si la valeur est dans l'intervalle

afficherChoix(message, choix) :
    affiche un message ainsi que l'ensemble des choix disponibles avec leur numéro associé

estDejaDansListe(liste, valeur):
    retourne si le personnage est contenue dans la liste

teamIsAlive():
    retourne si tous les personnages sont mort 

monstreIsAlive():
    retourne si le monstre est mort  

attaquer(personnage):
    soustrait aux pv du monstre la soustraction de l'attaque du personnage et la defense du monstre

attaqueDuMonstre():
    soustrait aux pv d'un personnage aléatoire vivant de l'équipe la soustraction de l'attaque du monstre et de la défense du personnage
     
MENU :
    AFFICHER LES CHOIX POSSIBLES :
        afficherChoix(message, choixMenu)
    tant que vrai : 
        récupérer le choix :
            vérifier le choix
            si isInRange(choixMenu, choix):
                retourner choix
            sinon :
                lancer fonction erreur
    JEU:
        CHOIX NOM UTILISATEUR:
            tant que vrai :
                récupérer le nom d'utilisateur:
                    Vérifier le nom 
                    si EmptyOrWhiteSpace(nomUtilisateur):
                        retourner choix
                    sinon :
                        lancer fonction erreur
        CREATION D'EQUIPE:
            tant que vrai :
                récupérer le nom d'utilisateur:
                    Vérifier le nom d'équipe
                    si isEmptyOrWhiteSpace(nomEquipe) :
                        retourner nomEquipe
                    sinon :
                        lancer fonction erreur
            Afficher équipe actuelle
            Choisir les personnages :
                Récupérer la liste des personnages:
                    ouvrir base
                    acceder à collection personnages
                Tant que nombre personnage < 3:
                Afficher liste personnages : 
                    afficherChoix(message, choixPersonnages)
                RECUPERER LE CHOIX : 
                    tant que vrai :
                        vérifier si le choix est valide
                        si isInRange(choixPersonnages, choix):
                            continuer
                        sinon :
                            lancer fonction erreur
                        vérifier si le personnage est deja pris
                        si estDejaDansListe(choixPersonnages,choix):
                            retourner choix
                        sinon :
                            lancer fonction erreur
        COMBAT : 
            Tant que teamIsAlive() :
                instancierMonstre()
                Tant que monstreIsAlive():
                    Pour chaques personnages :
                        si isAlive(personnage) :
                            attaquer(personnage)
                        si !monstreIsAlive():
                           incrementer le nombre de vague
                           passer a la prochaine boucle   
                    attaqueDuMonstre()
            Sauvegarder le nombre de vagues
            Afficher le nombre de vagues + afficher classement (juste après)

    CLASSEMENT:
        Afficher les score :
            Recupérer scores :
                ouvrir base
                accéder à la collection
                la convertir en liste
            Filtrer les scores : 
                trier le tableau
                récupérer les 3 éléments voulus
            retourner les éléments
        
    QUITTER:
        sys.exit()
        
"""
choixMenu = ["Démarrer le jeu", "Afficher le classement", "Quitter"]
nbVague = 1
pseudo = ""
def menu():
    option = choixNumerique("Veuillez choisir une option", choixMenu, valeurInterdite)
    if (option == 1):
        jeu()
    elif(option == 2):
        afficherClassement()
    elif(option == 3):
        quitter()

def jeu():
    personnages = chargerPersonnages()
    pseudo = choixTextuel("Veuillez choisir un pseudo", messageStringInvalide)
    equipe = creerEquipe(personnages)
    combat(equipe)


def combat(equipe):
    while teamIsAlive(equipe):
        monstre = genererMonstreAleatoire()
        while monstreIsAlive(monstre):
            for personnage in equipe:
                if(isAlive(personnage)):
                    attaquer(personnage, monstre)
                    if(not monstreIsAlive()):
                        nbVague += 1
                        #passer a la prochaine boucle du premier while
            attaqueDuMonstre(equipe,monstre)
    score = Score(1, pseudo, nbVague)
    insererScore(score)
    messageFinPartie()
    afficherClassement()
    

                





def afficherClassement():
    classement = chargerScores()
    for i in range(len(classement)):
        print(f"{i+1}-{classement[i].player_name}-{classement[i].waves}vagues")


def messageFinPartie():
    print(f"Fin de partie, vous avez vaincu {nbVague} vagues")

def messageStringInvalide():
    print("Nom invalide")

def valeurInterdite():
    print("Valeur non-autorisée")
def isInRange(tableauChoix, valeur):
    return (valeur >=1 & valeur <=len(tableauChoix))
def isEmptyOrWhiteSpace(string):
    return not string or not string.strip()

def creerEquipe(personnages):
    equipe = []
    while (len(equipe) < 3):
        indexPersonnage = choixNumerique("Veuillez choisir un personnage", personnages, valeurInterdite)
        if estDejaDansListe(personnages[indexPersonnage-1], equipe):
            print("ce personnage est deja dans l'équipe")
        else:
            equipe.append(personnages[indexPersonnage-1])
    return equipe


def choixNumerique(message,tableauChoix, fonctionErreur):
    while (True):
        for i in range(len(tableauChoix)):
            print(f"{i+1}-{tableauChoix[i]}")
        valeur = int(input(message))
        if(isInRange(tableauChoix , valeur)):
            return valeur
        else: fonctionErreur

def choixTextuel(message, fonctionErreur):
    while (True):
        valeur = str(input(message))
        if(isEmptyOrWhiteSpace(valeur)):
            fonctionErreur
        else :
            return valeur

def estDejaDansListe(personnage, equipe):
    for p in equipe:
        if (personnage.id == p.id):
            return True
    return False

def teamIsAlive(equipe):
    nbMort = 0
    for p in equipe:
        if(not p.isAlive()):
            nbMort +=1
    return nbMort == 3

def isAlive(personnage):
    return personnage.hp > 0

def getTeamAlive(equipe):
    return equipe.filter(lambda p : p.isAlive())

def monstreIsAlive(monstre):
    return monstre.pv > 0

def attaquer(personnage, monstre):
    monstre.hp -= (personnage.attack - monstre.defense) 

def attaqueDuMonstre(equipe, monstre):
    personnagesAttaquables = getTeamAlive(equipe)
    indexAleatoire = getNombreAleatoire(personnagesAttaquables)
    personnageCible = personnagesAttaquables[indexAleatoire]
    personnageCible.hp -= (monstre.attack - personnageCible.defense)

def quitter():
    sys.exit()


menu()