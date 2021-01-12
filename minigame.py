class minigame:
    def initialise(self):
        self.gameActive = False
        self.p1score = 0
        self.p1keyDown = False
        self.p2score = 0
        self.p2keyDown = False
        self.scoreLimit = 60
        self.winnerDecided = False
        self.winTimer = 0
        
    def show(self):
        fill(255)
        text(self.p1score, 50, 500)
        text(self.p2score, 750, 500)
        self.gameActive = True
        if self.p1score == self.scoreLimit and self.p2score == self.scoreLimit:
            self.scoreLimit += 1
        elif self.p1score == self.scoreLimit and self.p2score != self.scoreLimit:
            text('Player 1 wins', 400, 300)
            self.gameActive = False
            self.winnerDecided = True
        elif self.p1score != self.scoreLimit and self.p2score == self.scoreLimit:
            text('Player 2 wins', 400, 300)
            self.gameActive = False
            self.winnerDecided = True
            
    def reset(self):
        self.p1score = 0
        self.p2score = 0
        self.scoreLimit = 100
        self.winnerDecided = False
        self.winTimer = 0
