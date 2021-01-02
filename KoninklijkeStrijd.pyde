add_library('sound')
import Menu

def setup():
    size(800, 600)
    global sf, click
    sf = SoundFile(this,"menu.mp3")
    sf.play()
    Menu.setup()
    
    
def draw():
    Menu.draw()
  
def mouseClicked():
    Menu.mouseClicked()
