class Player:
    #initialiseert alle attributes van de class
    def __init__(self, name, health, colour):
        self.name = name
        self.health = health
        self.colour = colour
        #Load the heart png with the right colour
        self.heartImage = loadImage("heart_" + self.colour + ".png")
        self.banner =  loadImage("banner_" + self.colour + ".png")
        
    #Code om de speler te tekenen
    def show(self, x, y):
        image(self.banner, x - 50, y - 25, 194, 60)
        fill(255)
        #veranderd de kleur van de tekst zodra de speler geen levens meer heeft
        if self.health > 0:
            fill(255)
        else:
            fill(170, 0, 0)
        text(self.name, x, y)
        
        for i in range(self.health):
            #Place the image of the heart with on the right place.
            image(self.heartImage, (x - 40) + 30 * i, y + 8, 25, 25)
            #text("X", x + 20 * i, y + 20)
            
        
        
    
    
