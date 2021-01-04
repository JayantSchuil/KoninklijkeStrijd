from PlayerScreen import *

def setup():
    global playerScreen, startScreen
    size(800, 600)
    playerScreen = PlayerScreen()
    playerScreen.initialise()
    startScreen = IntroScreen()
    Menu.setup()

def draw():
    background(15)
    playerScreen.show()
    Menu.draw()
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
        
def mouseClicked():
    Menu.mouseClicked()
        
