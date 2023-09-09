import random


class Player:
    def __init__(self, name, roshambo_value=""):
        self.name = name
        self.roshambo_value = roshambo_value


class Bart(Player):
    def __init__(self, name="Bart", roshambo_value=""):
        Player.__init__(self, name, roshambo_value)

    def generate_roshambo(self):
        self.roshambo_value = "rock"


class Lisa(Player):
    def __init__(self, name="Lisa", roshambo_value=""):
        Player.__init__(self, name, roshambo_value)
        self.roshambo_values = ["rock", "paper", "scissors"]

    def generate_roshambo(self):
        self.roshambo_value = random.choice(self.roshambo_values)
