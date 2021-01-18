class minigame:
    def initialise(self):
        self.gameActive = False
        self.p1score = 0
        self.p1keyDown = False
        self.p2score = 0
        self.p2keyDown = False
        self.scoreLimit = 100
        self.winnerDecided = False
        self.winTimer = 0

    def show(self):
        fill(255)
        text(self.p1score, 50, 500)
        text('Spam Z', 50, 475)
        text(self.p2score, 750, 500)
        text('Spam M', 750, 475)
        self.gameActive = True
        if self.p1score == self.scoreLimit and self.p2score == self.scoreLimit:   #Als beide spelers tegelijkertijd bij 100 aankomen gaat het limiet omhoog
            self.scoreLimit += 1
        elif self.p1score == self.scoreLimit and self.p2score != self.scoreLimit: #Speler 1 komt het eerst bij 100 aan en wint
            text('Player 1 wins', 400, 300)
            self.gameActive = False
            self.winnerDecided = True
        elif self.p1score != self.scoreLimit and self.p2score == self.scoreLimit: #Speler 2 komt het eerst bij 100 aan en wint
            text('Player 2 wins', 400, 300)
            self.gameActive = False
            self.winnerDecided = True
            
    def reset(self):  #reset alle values naar default zodat de game opnieuw gespeeld kan worden
        self.p1score = 0
        self.p2score = 0
        self.scoreLimit = 60
        self.winnerDecided = False
        self.winTimer = 0
        

    
