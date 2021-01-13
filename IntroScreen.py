class IntroScreen:
    def  __init__(self):
        global IntroScreen
        self.intro = loadImage("intro.png")
        self.opacity = 0.0
        self.timer = 0
        self.interval = 5
        self.fadeOut = False
        self.SCREENSTATE = -1

    def show(self):
        self.opacity = self.opacity + self.interval
        if self.opacity > 255.0:
            if self.timer == 15:
                self.interval = -2.5
                self.fadeOut = True
            else:
                self.timer += 1
        elif self.fadeOut and self.opacity < 0.0:
            #set new status here
            self.SCREENSTATE = 0
            #print("Status = menu")
        image(self.intro, 0, 0)
        tint(255, self.opacity)
        if self.SCREENSTATE == 0:
            noTint()
