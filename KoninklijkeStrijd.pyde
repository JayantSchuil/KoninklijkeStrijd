from IntroScreen import *

def setup():
    global startScreen
    size(1200, 900)
    startScreen = IntroScreen()

def draw():
    background(loadImage("intro.png"))
    startScreen.show()
