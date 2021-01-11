add_library("sound")
from PlayerScreen import *
from IntroScreen import *
import Menu

def setup():
    global startScreen, sf, click
    size(800, 600)
    startScreen = IntroScreen()
    sf = SoundFile(this,"menu.mp3")
    click = SoundFile(this,"Click.mp3")
    sf.loop(1, 0.1)
    click.amp(0.2)
    sf.play()
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
    if Menu.mouseClicked:
        click.play()

    
