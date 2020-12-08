color_rec = 255
recglow = False
from Button import*

def setup():
    size(800, 600)
    global fight_button, credit_button
    fight_button = Button(400,200,165,55,'Fight')
    credit_button = Button(400,275,165,55,'Credit')
    
    
def draw():
    credit_button.show()
    fight_button.show()
    if fight_button.mouseOverButton():
        recglow()
    
    
    
    
def recglow():
    fill(color_rec)
    filter(BLUR, 4)
    stroke(0)
    smooth()
    fight_button.show()
    print(recglow)
    

    


        
        
        
