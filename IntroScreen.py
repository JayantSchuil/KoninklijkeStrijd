class IntroScreen:
    def  __init__(self):
        self.img = loadImage("intro.png")
        self.opacity = 0.0
        self.timer = 0
        self.interval = 1.8
        self.fadeOut = False

    def show(self):
        self.opacity = self.opacity + self.interval
        if self.opacity > 255.0:
            if self.timer == 48:
                self.interval = -2.5
                self.fadeOut = True
            else:
                self.timer += 1
        elif self.fadeOut and self.opacity < 0.0:
            #set new status here
            print("Status = menu")
        image(self.img, 0, 0)
        tint(255, self.opacity)
