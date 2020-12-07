class Button:
    def __init__(self, x, y, w, h, buttonText):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.buttonText = buttonText
    
    def show(self):
        rectMode(CENTER)
        fill(255)
        rect(self.x, self.y, self.w, self.h)
        fill(0)
        text(self.buttonText, self.x - 27, self.y + 5, 10)
    

    def mouseOverButton(self):
        if mouseX > self.x and mouseX < self.x + self.w:
            if mouseY > self.y and mouseY < self.y + self.h:
                return True
