from PlayerScreen import *
from IntroScreen import *
import Menu

def setup():
    global startScreen
    size(800, 600)
    startScreen = IntroScreen()
    Menu.setup()

def draw():
    background(15)
    startScreen.show()
    
def mousePressed():
    Menu.mousePressed()
        
def mouseReleased():
    Menu.mouseReleased()
        
def mouseClicked():
    Menu.mouseClicked()
        
