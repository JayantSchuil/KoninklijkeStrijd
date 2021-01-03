from IntroScreen import *
import Menu

def setup():
    size(800, 600)
    startScreen = IntroScreen()
    Menu.setup()
    
def draw():
    startScreen.show()
    Menu.draw()
  
def mouseClicked():
    Menu.mouseClicked()