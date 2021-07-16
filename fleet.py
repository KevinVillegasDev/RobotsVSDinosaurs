from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = self.create_fleet()
    
    def create_fleet(self):
        robot_one = Robot('DinoKiller', 100)
        robot_two = Robot('Tyrannachopper', 100)
        robot_three = Robot('Robolizard', 100)
        return [robot_one, robot_two, robot_three]