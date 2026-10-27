from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["temp"]  # Sélection ou création de la base test_db

personnages = db["personnages"]

for personnage in personnages.find():
    print(personnage)
