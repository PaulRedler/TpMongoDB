from random import randint

def getNombreAleatoire(max):
    return randint(1,max)

def recupererChoixNumerique(message,tableauChoix, fonctionErreur):
    while (True):
        valeur = int(input(f"{message}\n"))
        if(isInRange(tableauChoix , valeur)):
            return valeur
        else:
            fonctionErreur()

def recupererChoixTextuel(message, fonctionErreur):
    while (True):
        valeur = str(input(f"{message}\n"))
        if(isEmptyOrWhiteSpace(valeur)):
            fonctionErreur()
        else :
            return valeur

def afficherMessageFinPartie(nbVagues):
    print(f"Fin de partie, vous avez vaincu {nbVagues} vagues")

def afficherMessageStringInvalide():
    print("Nom invalide")

def afficherMessageEntierInvalide():
    print("Valeur non-autorisée")

def isInRange(tableauChoix, valeur):
    return (valeur >=1 & valeur <=len(tableauChoix))

def isEmptyOrWhiteSpace(string):
    return not string or not string.strip()

def formerMessageSelection(personnagesDisponibles):
    message = "Choissisez un personnage dans la liste \n"
    for index , personnage in enumerate(personnagesDisponibles):
        message += str(index+ 1) +"-"+ personnage.name +"\n"
    return message

def formerMessageMenu(choixMenu):
    messageMenu = "Veuillez choisir une option \n"
    for i in range(len(choixMenu)):
        messageMenu+= str(i+1) +"-"+ choixMenu[i] +"\n"
    return messageMenu