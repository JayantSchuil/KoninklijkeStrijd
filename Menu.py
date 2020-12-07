color_rec = 255

def setup():
    size(800, 600)
    
def draw():

    fill(color_rec)
    rect(315,300,150,55)
    texts('FIGHT', 350, 335)    
    
def texts(x,w,h):
    fill(0, 102, 153)
    textSize(23)
    text(x,w, h)
    
def mouseClicked():
    global color_rec
    if mouseX > 315 and mouseX < 315 + 150 and mouseY > 300 and mouseY < 300 + 55:
        color_rec = 0
        
        
