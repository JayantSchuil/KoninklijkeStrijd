class minigame:
    def initialise(self):
        self.p1score = 0
        self.p1keyDown = False
        self.p2score = 0
        self.p2keyDown = False
        
    def show(self):
        fill(255)
        text(self.p1score, 50, 500)
        text(self.p2score, 750, 500)
