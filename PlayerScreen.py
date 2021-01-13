#Author: Jayant Schuil - 1010841
from Player import *
from Button import *

class PlayerScreen:
    def __init__(self):
        print("Jeetje Joh.")
    
    def initialise(self):
        global player1, player2, player3, player4, buttonAtt, buttonBattle
        self.player1 = Player("Speler 1", 3, "green")
        self.player2 = Player("Speler 2", 3, "red")
        self.player3 = Player("Speler 3", 3, "yellow")
        self.player4 = Player("Speler 4", 3, "blue")
        self.buttonAtt = Button(width / 2, height / 2, 120, 60, "Val aan")
        self.buttonBattle = Button(width / 2, 450 / 2, 120, 60, "Vecht")
        
    def show(self):
        self.player1.show(50, 50)
        self.player2.show(width - 100, 50)
        self.player3.show(50, height - 40)
        self.player4.show(width - 100, height - 40)
        #Lelijke code om te checken of een speler gewonnen heeft
        if self.player1.health > 0 and self.player2.health == 0 and self.player3.health == 0 and self.player4.health == 0:
            fill(255)
            text(self.player1.name + " is de koning!", width/2, height/2)
            
        elif self.player2.health > 0 and self.player1.health == 0 and self.player3.health == 0 and self.player4.health == 0:
            fill(255)
            text(self.player2.name + " is de koning!", width/2, height/2)
        elif self.player3.health > 0 and self.player2.health == 0 and self.player1.health == 0 and self.player4.health == 0:
            fill(255)
            text(self.player3.name + " is de koning!", width/2, height/2)
        elif self.player4.health > 0 and self.player2.health == 0 and self.player3.health == 0 and self.player1.health == 0:
            fill(255)
            text(self.player4.name + " is de koning!", width/2, height/2)
        else:
            #Als er nog geen winnaar is runt deze code
            self.buttonAtt.show()
            self.buttonBattle.show()
