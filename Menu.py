color_rec = 255


def setup():
    size(800, 600)
    global pg
    pg = createGraphics(150, 55)
    
def draw():
    rectover = True if mouseX > 315 and mouseX < 315 + 150 and mouseY > 300 and mouseY < 300 + 55 else False 

    if rectover == True:
        fill(51)
    else: 
        fill(255)
    rec(315,300,150,55)
    if mouseX > 315 and mouseX < 315 + 150 and mouseY > 300 and mouseY < 300 + 55:
        recglow(315,300,150,55)
    texts('Credit', 350, 335)
    rectangle()
    rec(315,225,150,55)
    if mouseX > 315 and mouseX < 315 + 150 and mouseY > 225 and mouseY < 225 + 55:
        recglow(315,225,150,55)
    texts('FIGHT', 350, 260)
        
def rectangle():
    pg.beginDraw()
    pg.background(255)
    pg.stroke(0)
    pg.endDraw()
    image(pg, 200, 50)
    
def rec(w,h,sizew,sizeh): 
    global color_rec
    fill(color_rec)
    rect(w,h,sizew,sizeh)
   

def recglow(w,h,sizew,sizeh):
    global color_rec
    fill(color_rec)
    rect(w,h,sizew,sizeh)
    filter(BLUR, 4)
    stroke(0)
    smooth()
    
    
def texts(x,w,h):
    fill(0, 102, 153)
    textSize(23)
    text(x,w, h)
    



        
        
        
