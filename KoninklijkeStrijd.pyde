add_library("sound")
from PlayerScreen import *
from IntroScreen import *
import Menu

def setup():
    global startScreen, sf, click
    size(800, 600)
    startScreen = IntroScreen()
    sf = SoundFile(this,"menu.mp3")
    click = SoundFile(this,"click.wav")
    sf.loop(1, 0.3)
    click.amp(0.3)
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
    if Menu.mouseClicked:
        click.play()
    Menu.mouseClicked()
