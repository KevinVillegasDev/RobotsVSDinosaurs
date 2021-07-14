class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health #will be int
        self.weapon = weapon
        
    def attack(self, dinosaur):
        self.dinosaur = dinosaur