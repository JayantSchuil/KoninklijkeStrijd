SCREENSTATE = 0 

def setup():
    size(800, 600)
    global bg, SCREENSTATE


def draw():
    if (SCREENSTATE == 0):
        drawMenu()
    if (SCREENSTATE == 2):
        drawCredits() 
                            
def drawMenu(): 
    global SCREENSTATE 
    bg = loadImage('Castle1.gif')
    background(0)
    image(bg, 0, 0)
    texts('Battle', 675, 325)
    texts('Credits', 675, 375)
    noStroke()
    fill(0,50)
    rect(600, 300, 150, 200)
    mouseOver()
    
def drawCredits():
    global SCREENSTATE     
    bg = loadImage('Castle1.gif')
    background(0)
    image(bg, 0, 0)
    texts('Return', 675, 325)
    noStroke()
    fill(0,50)
    rect(600, 300, 150, 200) 
    if mouseX <= 703 and mouseX >= 646 and mouseY <= 323 and mouseY >= 309:
        texts('Return', 675, 325)
        fill(255)
    else:
        noStroke()
        fill('#c4d6e2')
   
def texts(x, pos1, pos2):
    fill('#c4d6e2')
    textSize(23)
    textAlign(CENTER)
    text(x, pos1, pos2)
  
def mouseOver():
    if mouseX <= 703 and mouseX >= 646 and mouseY <= 323 and mouseY >= 309:
        texts('Battle', 675, 325)
        fill(255)
    if mouseX <= 711 and mouseX >= 639 and mouseY <= 372 and mouseY >= 360:
        texts('Credits', 675, 375) 
        fill(255) 
    else: 
        noStroke()
        fill('#c4d6e2')

def mouseClicked():
    global SCREENSTATE
    if SCREENSTATE == 0 and mouseX <= 711 and mouseX >= 639 and mouseY <= 372 and mouseY >= 360: #Credits
        SCREENSTATE = 2
    if SCREENSTATE == 0 and mouseX >= 646 and mouseY <= 323 and mouseY >= 309: #Battle 
        SCREENSTATE = 0
    if SCREENSTATE == 2 and mouseX >= 646 and mouseY <= 323 and mouseY >= 309: #Return
        SCREENSTATE = 0

        
        
        
