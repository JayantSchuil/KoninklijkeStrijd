from Button import *

class IntroScreen():
    def  __init__(self):
        global startButton
        startButton = Button(600, 800, 80, 40, "Start")

    def show(self):
        startButton.show()
