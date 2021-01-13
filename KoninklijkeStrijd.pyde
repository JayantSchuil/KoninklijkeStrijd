#Author: Sharoek Mahboeb - 1018492
add_library("sound")
add_library('gifAnimation')
from IntroScreen import *
from PlayerScreen import *
from minigame import *
SCREENSTATE = -1
x = -100
time = '3'
interval = 3
start = 'OFF'
index = 0
test = 0
idleOn = 'ON'
idle2On = 'ON'



def setup():
    global loopingGif, startScreen, sf, click, SCREENSTATE, playerScreen, start, minigame,attack1, idle, attack2, attack1, idle2
 
    size(800, 600)
    frameRate(27)
    playerScreen = PlayerScreen()
    playerScreen.initialise()
    minigame = minigame()
    minigame.initialise()
    startScreen = IntroScreen()
    sf = SoundFile(this,"menu.mp3")
    click = SoundFile(this,"Click.mp3")
    sf.loop(1, 0.1)
    click.amp(0.2)
    sf.play()
    attack1 = [loadImage('Slashing_' + str(i) + '.png') for i in range (1,12)]
    attack2 = [loadImage('Slashing1_' + str(i) + '.png') for i in range (1,12)]
    idle = [loadImage('Idle Blinking_' + str(i) + '.png') for i in range (1,18)]
    idle2 = [loadImage('Idle1_' + str(i) + '.png') for i in range (1,18)]
    loopingGif = Gif(this, 'bg2.gif')
    loopingGif.loop()
    loopingGif.play()


def draw():
    global start, interval, begin, minigame, SCREENSTATE,test, idle2, idle2On, idleOn, idle, loopingGif
    if SCREENSTATE == -1:
        background(15)
    else:
        background(loopingGif)
    if (SCREENSTATE == -1):
        startScreen.show()
        if startScreen.SCREENSTATE == 0:
            SCREENSTATE = 0   
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
    if (SCREENSTATE == 4):
        minigame.show()
        if idleOn == 'ON':
            image(idle[test%17], 325,300)
            test += 1
        if idle2On == 'ON':
            image(idle2[test%17], 375,300)
            test += 1 
        if minigame.winnerDecided:
            if minigame.winTimer >= 60:
                minigame.reset()
                SCREENSTATE = 1
            else:
                minigame.winTimer += 1
                
def sprite():
    global attack1, index,idleOn
    if key == 'z':
        image(attack1[index%11],325,300)
        index += 12
    if key == 'm':
        image(attack2[index%11],375,300)
        index += 12                
                

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
    global start, time, SCREENSTATE
    t = interval-int(millis()-begin)/1000
    time = nf(t, 1)   
    text(time,400,75)
    if time == '0':
        start = 'OFF'
        SCREENSTATE = 4                    
                                    
        
def mousePressed():
    global selectedPlayer, SCREENSTATE
    if SCREENSTATE ==1: 
        if mouseX < 70 and mouseX > 10 and mouseY < 49 and mouseY > 35: #Speler 1
            selectedPlayer = playerScreen.player1
            print(selectedPlayer.name)
        elif mouseX < 732 and mouseX > 667 and mouseY < 49 and mouseY > 35: #Speler 2
            selectedPlayer = playerScreen.player2
            print(selectedPlayer.name)
        elif mouseX < 87 and mouseX > 10 and mouseY > 543  and mouseY < 562: #Speler 3
            selectedPlayer = playerScreen.player3
            print(selectedPlayer.name)
        elif mouseX < 730 and mouseX > 670 and mouseY > 543 and mouseY < 562  : #Speler 4
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
        
def mouseClicked():
    global SCREENSTATE
    click.play()
    if SCREENSTATE == 0 and mouseX <= 707 and mouseX >= 639 and mouseY <= 372 and mouseY >= 360: #Credits
        SCREENSTATE = 2
    elif SCREENSTATE == 2 or SCREENSTATE == 1 and mouseX >= 646 and mouseX <= 706 and mouseY <= 323 and mouseY >= 309: #Return
        SCREENSTATE = 0
    elif SCREENSTATE == 0 and mouseX >= 625 and mouseX <= 747 and mouseY <= 423 and mouseY >= 411: #Quit Game 
        SCREENSTATE = 3    
    elif SCREENSTATE == 0 and mouseX >= 651 and mouseX <= 699  and mouseY <= 323 and mouseY >= 309:#battle 
        SCREENSTATE = 1 

def keyPressed():
    global idleOn, idle2On
    if SCREENSTATE == 4 and minigame.gameActive:
        if key == 'z' and not minigame.p1keyDown:
            minigame.p1score += 1
            minigame.p1keyDown = True
            sprite()
        if key == 'm' and not minigame.p2keyDown:
            minigame.p2score += 1
            minigame.p2keyDown = True
            sprite()
    
def keyReleased():
    global idleOn, idle2On
    if SCREENSTATE == 4 and minigame.gameActive:
        idle2On = 'ON'
        idleOn = 'ON'
        if key == 'z' and minigame.p1keyDown:
            minigame.p1keyDown = False
           
        if key == 'm' and minigame.p2keyDown:
            minigame.p2keyDown = False
            
