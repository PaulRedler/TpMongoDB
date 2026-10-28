from pymongo import MongoClient
from models import *
from utils import *
client = MongoClient("mongodb://localhost:27017")
db = client["temp"]  # Sélection ou création de la base test_db

def chargerPersonnages():
    personnagesEnBase = db["personnages"]
    listePersonnages = []
    for p in personnagesEnBase.find():
        perso = Personnage(p["_id"], p["name"], p["attack"], p["defense"], p["hp"])
        listePersonnages.append(perso)
    return listePersonnages

def genererMonstreAleatoire():
    monstresEnBase = db["monstres"]
    listeMonstres = []
    for m in monstresEnBase.find():
        monstre = Monstre(m["_id"], m["name"], m["attack"], m["defense"], m["hp"])
        listeMonstres.append(monstre)
    monstre = listeMonstres[getNombreAleatoire(listeMonstres.length)]
    print (f"le monstre est {monstre.name}, il a {monstre.hp} pv")
    return monstre

def chargerScores():
    scoresEnBase = db["scores"]
    listeScores = []
    for s in scoresEnBase :
        score = Score(s["_id"], s["player_name"], s["waves"])
        listeScores.append(score)
    listeOrdonee = sorted(listeScores, key = lambda s : s.score)
    return [listeOrdonee[-3:-1]]

def insererScore(score):
    scoresEnBase = db["scores"]
    result = scoresEnBase.insert_one(score)
    print("Inserted document ID:", result.inserted_id)

    
        
