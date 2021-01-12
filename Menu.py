from PlayerScreen import *
SCREENSTATE = 0 
bgIndex = 0
x = -100
time = '3'
interval = 3

def setup():
    global bg, SCREENSTATE, bgImages, playerScreen, start
    frameRate(27)
    bgImages = [loadImage(str(i).zfill(3) + ".jpg") for i in range(10, 191)]
    playerScreen = PlayerScreen()
    playerScreen.initialise()
    start = 'OFF'
    
def draw():
    global bgIndex, start, interval, begin
    background(bgImages[bgIndex%181])
    bgIndex += 1
    if (SCREENSTATE == 0):
        drawMenu()
    if (SCREENSTATE == 1):
        playerScreen.show()
        if start == 'ON':
            timer()
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
    if x == 900:
        x = -100 
    texts('Intro:', 400 , x - 275)   
    texts('Dennis', 400 , x - 250)   
    texts('Battle:', 400 , x - 200)    
    texts('Jayant', 400 , x - 175)    
    texts('Faraaz', 400 , x - 150)   
    texts('Menu & Sound:', 400 , x - 100)    
    texts('Sharoek', 400 , x - 75)      
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

def timer():
    t = interval-int(millis()-begin)/1000
    time = nf(t, 1)    
    text(time,400,100)


def mouseClicked():
    global SCREENSTATE
    if SCREENSTATE == 0 and mouseX <= 707 and mouseX >= 639 and mouseY <= 372 and mouseY >= 360: #Credits
        SCREENSTATE = 2
    elif SCREENSTATE == 2 or SCREENSTATE == 1 and mouseX >= 646 and mouseX <= 706 and mouseY <= 323 and mouseY >= 309: #Return
        SCREENSTATE = 0
    elif SCREENSTATE == 0 and mouseX >= 625 and mouseX <= 747 and mouseY <= 423 and mouseY >= 411: #Quit Game 
        SCREENSTATE = 3    
    elif SCREENSTATE == 0 and mouseX >= 651 and mouseX <= 699  and mouseY <= 323 and mouseY >= 309:#battle 
        SCREENSTATE = 1   

    

        
def mousePressed():
    global selectedPlayer, SCREENSTATE
    if SCREENSTATE ==1: 
        if mouseX < 70 and mouseX > 10 and mouseY < 20 and mouseY > 6: #Jayant
            selectedPlayer = playerScreen.player1
            print(selectedPlayer.name)
        elif mouseX < 732 and mouseX > 667 and mouseY < 20 and mouseY > 6: #Dennis
            selectedPlayer = playerScreen.player2
            print(selectedPlayer.name)
        elif mouseX < 87 and mouseX > 10 and mouseY >556  and mouseY < 569: #sharoek
            selectedPlayer = playerScreen.player3
            print(selectedPlayer.name)
        elif mouseX < 730 and mouseX > 670 and mouseY > 556 and mouseY < 569  : #Faraaz
            selectedPlayer = playerScreen.player4
            print(selectedPlayer.name) 


def mouseReleased():
    global SCREENSTATE , start, begin    
    if SCREENSTATE ==1: 
        try: 
            if playerScreen.buttonAtt.mouseOverButton():
                selectedPlayer.health -= 1 
            if playerScreen.buttonBattle.mouseOverButton():
                if start == 'OFF':
                    start = 'ON'
                    begin = millis()                
        except:
            if playerScreen.buttonAtt.mouseOverButton():
                pass
