from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.Dinosaur = []
    
    def create_herd(self):
        dino_one = Dinosaur('Tyrannaroar', 25, 100)
        dino_two = Dinosaur('Longneckswinger', 25, 100)
        dino_three = Dinosaur('WaterDino', 25, 100)
        self.Dinosaur = [dino_one, dino_two, dino_three]