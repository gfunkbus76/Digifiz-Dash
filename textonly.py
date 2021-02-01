import os

#import RPi.GPIO as GPIO
from typing import Tuple

'''import constants used by pygame such as event type = QUIT'''
import pygame.locals

'''Vehicle Information'''
vehicle_owner = "Gavin"
digifiz_ver = "0.1"
number_points_speedsensor = 2
wheelcircumference = 0.000378788  # miles

size = (1920, 720)
indHL = (236, 253, 147)

path_to_folder = "~/Users/Gavin/Documents/Digifiz-Dash/"


'''GPIO State Variables''' # 0 off, 1 on
illuminationState = 0 # headlights to GPIO pin?
highbeamState = 0 # 0 off, 1 on
glowplugState = 0
brakelightState = 0
oilwarnState = 0
alternatoreState = 0
defrostState = 0
foglight_State = 0
lefturnState = 0
rightturnState = 0
#engine_tempstate = 8
#odo_state = 1  # 1 = display odometer, 0 = display tripometer

'''GPIO Pin Definitions'''
headlightPin = 22
highbeamPin = 21
glowplugPin = 23
brakelightPin = 24
oilwarnPin = 25
alternatorPin = 26
defrostPin = 27
foglightPin = 28
lefturnPin = 29
rightturnPin = 30

''' Variables ''' # setting variables to 0 at startup?
temp_coolant = "0"
temp_egt = "0"
temp_interior = "0"
speed_gps = "0"
speed_cv = "0"
press_oil = "0"
press_boost = "0"
rpm = "0"

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)


programIcon = pygame.image.load('images/speedometer.png')
pygame.display.set_icon(programIcon)


'''
Centres the pygame window. Note that the environment variable is called 
SDL_VIDEO_WINDOW_POS because pygame uses SDL (standard direct media layer)
for it's graphics, and other functions
'''
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

# Title
pygame.display.set_caption("Digifiz Dashboard v" + digifiz_ver)

'''Create variables with image names we will use'''
background = pygame.image.load("images/textbackground.png")
illuminationOn = pygame.image.load("images/illuminationOn.png").convert_alpha()
illuminationOff = pygame.image.load("images/illuminationOff.png").convert_alpha()
rpm200 = pygame.image.load("images/RPM 200.png").convert_alpha()


'''Used to manage how fast the screen updates'''
clock = pygame.time.Clock()

'''Display Font'''
font_path = "fonts/DSEG7Classic-Bold.ttf"
font_size = 174
fontObj = pygame.font.Font(font_path, font_size)

# Main Loop
running = True
while running:

    # Background image
    screen.blit(background, (0, 0))

    # # # Speedometer Font Testing ###
    # Speed in hundreds
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render("1", 1, indHL)
    #speedtext_rect = speedtext.get_rect()
    #speedtext_rect.right = 435
    #screen.blit(speedtext, (828,217), speedtext_rect)
    screen.blit(speedtext, (281, 131))

    # Speed in tens
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render("2", 0, indHL)
    screen.blit(speedtext, (962, 217))
    # Speed in singles
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render("8", 0, indHL)
    screen.blit(speedtext, (1104, 217))
    # pygame.display.flip()

    # Testing the RPM gauge
  #  if rpmstate == 12:
   #     screen.blit(rpm200, (132, 4))




    #testing the illumination button

    if illuminationState == 0:
        screen.blit(illuminationOn, (42, 627))
    #   GPIO.output(lightbarpin, False)
    #else:
    #    screen.blit(illuminationOff, (45, 460))
    #   GPIO.output(lightbarpin, True)
    #   pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    # screen.fill((255, 0, 0))
    #   pygame.display.update()
