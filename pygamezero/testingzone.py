
WIDTH = 1920
HEIGHT = 720
BACKGROUND_IMG = "textbackground"

illuminate = Actor ("illuminationoff")
illuminate.topleft = 42,627
illuminate.status = False

def draw():
    screen.blit(BACKGROUND_IMG, (0,0))
    illuminate.draw()
    
def update():
    pass
    
def set_illumination_on():
    illuminate.image = "illuminationon"
def set_illumination_off():
    illuminate.image = "illuminationoff"


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        if illuminate.collidepoint(pos):
            illuminate.status = True
            set_illumination_on()
        else:
            illuminate.status = False
            set_illumination_off
        
#def update():

