from PlayerScreen import *
from IntroScreen import *

def setup():
    global playerScreen, startScreen
    size(1000, 700)
    startScreen = IntroScreen()
    playerScreen = PlayerScreen()
    playerScreen.initialise()

def draw():
    background(255)
    playerScreen.show()
    startScreen.show()
    
def mousePressed():
    global selectedPlayer
    if mouseX < width/2 - 100 and mouseY < height/2 - 100:
        selectedPlayer = playerScreen.player1
        print(selectedPlayer.name)
    elif mouseX > width/2 + 100 and mouseY < height/2 - 100:
        selectedPlayer = playerScreen.player2
        print(selectedPlayer.name)
    elif mouseX < width/2 - 100 and mouseY > height/2 + 100:
        selectedPlayer = playerScreen.player3
        print(selectedPlayer.name)
    elif mouseX > width/2 + 100 and mouseY > height/2 - 100:
        selectedPlayer = playerScreen.player4
        print(selectedPlayer.name)
        
def mouseReleased():
    if playerScreen.buttonAtt.mouseOverButton():
        selectedPlayer.health -= 1
