from Button import *

class IntroScreen:
    def  __init__(self):
        self.startButton = Button(600, 800, 80, 40, "Start")

    def show(self):
        background(loadImage("intro.png"))
        self.startButton.show()
