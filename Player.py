class Player:
    def __init__(self, name, health, colour):
        self.name = name
        self.health = health
        self.colour = colour
        #Load the heart png with the right colour
        self.heartImage = loadImage("heart_red.png")

    def show(self, x, y):
        fill(255)
        text(self.name, x, y)
        for i in range(self.health):
            #Place the image of the heart with on the right place.
            # image(self.heartImage, x + 17 * i, y + 15, 15, 15)
            text("X", x + 20 * i, y + 20)

        
    
    
