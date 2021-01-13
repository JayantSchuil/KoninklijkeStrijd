class Player:
    #initialiseert alle attributes van de class
    def __init__(self, name, health, colour):
        self.name = name
        self.health = health
        #Load the heart png with the right colour
        self.heartImageBlue = loadImage("heart_blue" + ".png")
        self.heartImageGreen = loadImage("heart_green" + ".png") 
        self.heartImageRed = loadImage("heart_red" + ".png")
        self.heartImageYellow = loadImage("heart_yellow" + ".png")
        
    #Code om de speler te tekenen
    def show(self, x, y):
        # image(self.banner, x, y)
        fill(255)
        #veranderd de kleur van de tekst zodra de speler geen levens meer heeft
        if self.health > 0:
            fill(255)
        else:
            fill(170, 0, 0)
        text(self.name, x, y)
        
        for i in range(self.health):
            #Place the image of the heart with on the right place.
            image(self.heartImageBlue, x + 17 * i, y + 15, 15, 15)
            #text("X", x + 20 * i, y + 20)
            
        
        
    
    
