from db_init import chargerScores
def afficherClassement():
    classement = chargerScores()
    for i in range(len(classement)):
        print(f"{i+1}-{classement[i].player_name}-{classement[i].waves}vagues")
