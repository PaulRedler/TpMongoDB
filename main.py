"""
choixMenu = ["Démarrer le jeu", "Afficher le classement", "Quitter"]
choixPersonnages = GetListePersonnages()

isEmptyOrWhiteSpace(chaine):
    retourne si la chaine est vide ou ne contient que des espaces

isInRange(tableauChoix,valeur):
    retourne si la valeur est dans l'intervalle

afficherChoix(message, choix) :
    affiche un message ainsi que l'ensemble des choix disponibles

estDejaDansListe(liste, valeur):
    retourne si le personnage est contenue dans la liste

teamIsAlive():
    retourne si tous les personnages sont mort 

monstreIsAlive():
    retourne si le monstre est mort        
     
MENU :
    AFFICHER LES CHOIX POSSIBLES :
        afficherChoix(message, choixMenu)
    RECUPERER LE CHOIX : 
        tant que vrai :
            vérifier le choix :
                isInRange(choixMenu, choix)
    JEU:
        CHOIX NOM UTILISATEUR:
            Récupérer le nom d'utilisateur :
                Tant que vrai:
                    Vérifier le nom :
                       EmptyOrWhiteSpace(nomUtilisateur)
        CREATION D'EQUIPE:
            Récupérer le nom d'équipe :
                Tant que vrai:
                    Vérifier le nom d'équipe:
                        isEmptyOrWhiteSpace(nomEquipe)
            Afficher équipe actuelle
            Choisir les personnages :
                Tant que nombre personnage < 3:
                Afficher liste personnages : 
                    afficherChoix(message, choixPersonnages)
                RECUPERER LE CHOIX : 
                    tant que vrai :
                        vérifier si le choix est valide:
                            isInRange(choixPersonnages, choix)
                        vérifier si le personnage est deja pris :
                            estDejaDansListe(choixPersonnages,choix)
        COMBAT : 
            Tant que teamIsAlive() :
                instancierMonstre()
                Tant que monstreIsAlive():
                    Pour chaques personnages :
                        attaquer(personnage)
                        si !monstreIsAlive():
                           incrementer le nombre de vague
                           passer a la prochaine boucle   
                    attaqueDuMonstre()
            Sauvegarder le nombre de vagues
            Afficher le nombre de vagues + afficher classement 

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
        
"""