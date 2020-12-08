from Player import *
from Button import *

class PlayerScreen:
    def __init__(self):
        print("Jeetje Joh")
    
    def initialise(self):
        global player1, player2, player3, player4, buttonAtt, buttonBattle
        self.player1 = Player("Jayant", 3, "green")
        self.player2 = Player("Dennis", 3, "red")
        self.player3 = Player("Constantijn", 3, "yellow")
        self.player4 = Player("Faraaz", 3, "blue")
        self.buttonAtt = Button(500, 350, 75, 40, "Val aan")
        self.buttonBattle = Button(500, 400, 75, 40, "Vecht")
        
    def show(self):
        self.player1.show(10, 20)
        self.player2.show(950, 20)
        self.player3.show(10, 650)
        self.player4.show(950, 650)
        self.buttonAtt.show()
        self.buttonBattle.show()
