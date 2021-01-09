from Player import *
from Button import *

class PlayerScreen:
    def __init__(self):
         print("Jeetje Joh.")
    
    def initialise(self):
        global player1, player2, player3, player4, buttonAtt, buttonBattle
        self.player1 = Player("Jayant", 3, "green")
        self.player2 = Player("Dennis", 3, "red")
        self.player3 = Player("Sharoek", 3, "yellow")
        self.player4 = Player("Faraaz", 3, "blue")
        self.buttonAtt = Button(width / 2, height / 2, 120, 60, "Val aan")
        self.buttonBattle = Button(width / 2, 450 / 2, 120, 60, "Vecht")

        
    def show(self):
        self.player1.show(40, 20)
        self.player2.show(width - 100, 20)
        self.player3.show(50, height - 30)
        self.player4.show(width - 100, height - 30)
        self.buttonAtt.show()
        self.buttonBattle.show()
        fill('#c4d6e2')
        textSize(20)
        textAlign(CENTER)
        text('Return', 600, 325)

    
