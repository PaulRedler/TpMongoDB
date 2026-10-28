class Personnage:
    def __init__(self, id, name,attack, defense, hp ):
        self.id = id  
        self.name = name  
        self.attack = attack
        self.defense = defense
        self.hp = hp
class Monstre :
    def __init__(self, id, name, attack, defense, hp):
        self.id = id
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp

class Score :
    def __init__(self, id, player_name, waves):
        self.id = id
        self.player_name = player_name
        self.waves = waves
    
