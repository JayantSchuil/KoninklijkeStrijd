class Player:
    def __init__(self, name, health, colour):
        self.name = name
        self.health = health
        self.heartImageBlue = loadImage("heart_blue" + ".png")
        self.heartImageGreen = loadImage("heart_green" + ".png") 
        self.heartImageRed = loadImage("heart_red" + ".png")
        self.heartImageYellow = loadImage("heart_yellow" + ".png")

    def show(self, x, y):
        fill(255)
        text(self.name, x, y)
        for i in range(self.health):
            #Place the image of the heart with on the right place.
            image(self.heartImageBlue, x + 17 * i, y + 15, 15, 15)
            #text("X", x + 20 * i, y + 20)


        
    
    
