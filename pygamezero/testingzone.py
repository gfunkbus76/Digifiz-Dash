
WIDTH = 1920
HEIGHT = 720
BACKGROUND_IMG = "textbackground"

illuminate = Actor ("illuminationoff")
illuminate.topleft = 42,627

def draw():
    screen.blit(BACKGROUND_IMG, (0,0))
    illuminate.draw()
    
def set_illumination_on():
    illuminate.image = "illuminationon"
def set_illumination_off():
    illuminate.image = "illuminationoff"


def on_mouse_down(pos):
    if illuminate.collidepoint(pos):
        set_illumination_on()
        
        
#def update():

