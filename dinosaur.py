class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
    
    def attack(self, robot):
        if (robot.health != 0):
            robot.health = robot.health - self.attack_power
        