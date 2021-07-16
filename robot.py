from weapon import Weapon
import random

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health #will be int
        self.weapons = self.weapon_populate()
        self.weapon_choice = self.select_weapons()
        
    def attack(self, Dinosaur):
        if (Dinosaur.health != 0):
            Dinosaur.health = Dinosaur.health - self.weapon.attack_power
    
    def select_weapons(self):
        return random.choice(self.weapons)
    
    def weapon_populate(self):
        chainsaw = Weapon('', 25)
        raygun = Weapon('Raygun', 25)
        astroid_launcher = Weapon('AstroidLauncher', 25)
        return [chainsaw, raygun, astroid_launcher]