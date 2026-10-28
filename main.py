import sys
from utils import *
from db_init import * 
from game import jeu
from classement import afficherClassement

choixMenu = ["Démarrer le jeu", "Afficher le classement", "Quitter"]

def menu():
    message = formerMessageMenu(choixMenu)
    option = recupererChoixNumerique(message, choixMenu, afficherMessageEntierInvalide)
    if (option == 1):
        jeu()
    elif(option == 2):
        afficherClassement()
        menu()
    elif(option == 3):
        quitter()

def quitter():
    sys.exit()

menu()

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