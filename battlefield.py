# Step 1- Going to start game.
# Step 2- Going to display a welcome message to user
# Step 3- Going to start the actual battle
# Step 4- Each dinosaur will have a turn
# Step 5- Each robot will have a turn
# Step 6- After every attack, opponent will lose HP based on attack power of weapon for robot/attack power for dino
# Step 7- Display the dinosaurs opponents option for attack
# Step 8- Display the robots opponents options for attack
# Step 9- Display winners once either all dinos are dead or all robots are dead
from weapon import Weapon
from robot import Robot
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.Fleet = Fleet()
        self.Herd = Herd()
        
    
    def run_game(self):
        # while Herd[0].health != 0 and Fleet[0].health != 0:
        print(self.Fleet.robots[0].weapon_choice)  
            
    
    
    # def display_welcome(self):
    #     print("Welcome to your battlefield, RoboFleet and DinoHerd! Prepare for battle!")
    
    # def battle(self):
        
        
        
        
        
    # def dino_turn(self, dinosaur):
        
            
             
    
    
    # def robo_turn(self, robot):
    
    
    # def show_dino_opponent_options(self):
    
    
    # def show_robo_opponent_options(self):
    
    
    # def display_winners(self):
    
