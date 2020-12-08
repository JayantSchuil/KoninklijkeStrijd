from PlayerScreen import *

def setup():
    global playerScreen
    size(1000, 700)
    playerScreen = PlayerScreen()
    playerScreen.initialise()
    player4 = Player("Faraaz", 3)

def draw():
    background(15)
    playerScreen.show()
    
def mousePressed():
    global selectedPlayer
    if mouseX < width/2 - 100 and mouseY < height/2 - 100:
        selectedPlayer = playerScreen.player1
        print("Jayant")
    elif mouseX > width/2 + 100 and mouseY < height/2 - 100:
        selectedPlayer = playerScreen.player2
        print("Dennis")
    elif mouseX < width/2 - 100 and mouseY > height/2 + 100:
        selectedPlayer = playerScreen.player3
        print("Constantijn")
    elif mouseX > width/2 + 100 and mouseY > height/2 - 100:
        selectedPlayer = playerScreen.player4
        print("Faraaz")
        
def mouseReleased():
    if playerScreen.buttonAtt.mouseOverButton():
        selectedPlayer.health -= 1
        
    
        
