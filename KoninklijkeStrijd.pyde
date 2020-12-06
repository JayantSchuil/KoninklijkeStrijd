from Player import *
from Button import *

def setup():
    global player1, player2, player3, player4, buttonAtt
    size(1000, 700)
    player1 = Player("Jayant", 3)
    player2 = Player("Dennis", 3)
    player3 = Player("Constantijn", 3)
    player4 = Player("Faraaz", 3)
    buttonAtt = Button(500, 350, 75, 40, "Val aan")

    
    

def draw():
    background(15)
    player1.show(10, 20)
    player2.show(950, 20)
    player3.show(10, 650)
    player4.show(950, 650)
    buttonAtt.show()

        
