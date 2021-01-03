from IntroScreen import *
import Menu

def setup():
    size(800, 600)
    global startScreen
    startScreen = IntroScreen()
    Menu.setup()
    
def draw():
    Menu.draw()
    startScreen.show()
  
def mouseClicked():
    Menu.mouseClicked()
