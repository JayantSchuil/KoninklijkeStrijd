class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show(self, x, y):
        fill(255)
        text(self.name, x, y)
        for i in range(self.health):
            text("X", x + 10 * i, y + 15)

        
    
    
