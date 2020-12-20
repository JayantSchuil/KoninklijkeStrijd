SCREENSTATE = 0 
bgIndex = 0
x = -100

def setup():
    size(800, 600)
    global bg, SCREENSTATE, bgImages
    frameRate(25)
    bgImages = [loadImage(str(i).zfill(3) + ".jpg") for i in range(10, 191)]
        
def draw():
    global bgIndex
    background(bgImages[bgIndex%181])
    bgIndex += 1
    if (SCREENSTATE == 0):
        drawMenu()
    if (SCREENSTATE == 2):
        drawCredits() 
    if (SCREENSTATE == 3):
        exit()
                            
def drawMenu(): 
    global SCREENSTATE, bgIndex
    texts('Battle', 675, 325)
    texts('Credits', 675, 375)
    texts('Quit Game', 675, 425)
    noStroke()
    fill(0,50)
    rect(600, 300, 150, 200)
    mouseOver()
    
def drawCredits():
    global SCREENSTATE, bgIndex,x   
    texts('Return', 675, 325)
    noStroke()
    fill(0,50)
    rect(600, 300, 150, 200)
    if x == 620:
        x = -100 
    texts('Gemaakt door:', 400 , x)
    texts('Sharoek', 400 , x + 25)
    texts('Jayant', 400 , x + 50)
    texts('Dennis', 400 , x + 75)
    texts('Faraaz', 400 , x + 100)
    x += 5   
    if mouseX <= 703 and mouseX >= 646 and mouseY <= 323 and mouseY >= 309:
        texts('Return', 675, 325)
        fill(255)
    else:
        noStroke()
        fill('#c4d6e2')
   
def texts(x, pos1, pos2):
    fill('#c4d6e2')
    textSize(20)
    textAlign(CENTER)
    text(x, pos1, pos2)
  
def mouseOver():
    if mouseX <= 725 and mouseX >= 625 and mouseY <= 423 and mouseY >= 411:
        texts('Quit Game', 675, 425)
        fill(255)
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
    if SCREENSTATE == 0 and mouseX >= 625 and mouseY <= 423 and mouseY >= 411: #Quit Game 
        SCREENSTATE = 3
    

        
        
        
