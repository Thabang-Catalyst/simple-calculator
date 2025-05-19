# Base class
class SoccerPlayer:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

    def introduce(self):
        print(f"I am {self.name}, I play as a {self.position} for {self.team}!")

    def passing(self):
        print(f"{self.name} is very good at playing as a {self.position}.")

# Inherited class
class WorldClassPlayer(SoccerPlayer):
    def __init__(self, name, position, team, shooting_accuracy):
        super().__init__(name, position, team)
        self.shooting_accuracy = shooting_accuracy

    def introduce(self):
        print(f"I am {self.name}, a world-class {self.position} with {self.shooting_accuracy}% shooting accuracy. I play for {self.team}!")

    def shoot(self):
        print(f"{self.name} shoots with {self.shooting_accuracy}% accuracy!")

# Create objects
player1 = SoccerPlayer("Relebohile Mofokeng", "winger", "Orlando Pirates")
player2 = WorldClassPlayer("Victor Osimhen", "striker", "Galatasaray", 85)

# Call methods
player1.introduce()
player1.passing()

player2.introduce()
player2.passing()
player2.shoot()
