#Author: Jayant Schuil - 1010841

class Player:
    #initialiseert alle attributes van de class
    def __init__(self, name, health, colour):
        self.name = name
        self.health = health
        self.colour = colour
        #Load the heart png with the right colour
        self.heartImage = loadImage("images/heart_" + self.colour + ".png")
        self.banner = loadImage("images/banner_" + self.colour + ".png")
        
    #Code om de speler te tekenen
    def show(self, x, y):
        # image(self.banner, x, y)
        fill(0,50)
        #achtergrondje zodat de tekst meer opvalt tegen de achergrond van het programma
        rect(x, y, 150, 100)
        #veranderd de kleur van de tekst zodra de speler geen levens meer heeft
        if self.health > 0:
            fill(255)
        else:
            fill(170, 0, 0)
        text(self.name, x, y)
        for i in range(self.health):
            #Place the image of the heart with on the right place.
            # image(self.heartImage, x + 17 * i, y + 15, 15, 15)
            text("X", x + 20 * i, y + 20)

        
    
    
