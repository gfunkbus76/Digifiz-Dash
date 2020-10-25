from typing import Union

import pygame, sys, random, os, time, datetime

# import RPi.GPIO as GPIO
from pygame import Surface
from pygame.surface import SurfaceType

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

'''GPIO State Variables'''
illuminationState = 0
highbeamState = 0
lightbarstate = 0
wiperstate = 0
wiperplusstate = 0
wiperminusstate = 0
hornstate = 0
rpmstate = 12
engine_tempstate = 8
odo_state = 1  # 1 = display odometer, 0 = display tripometer

''' Arduino Variables '''
displayed_speed = "11"
rpm_level_arduino = "0" #note: this value from pi is a raw dump of the adc from 0 to 1024 (630=emplty, 210=full)


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

# Create the screen
# screen = pygame.display.set_mode((1920, 720), 0, 32)

# Title
pygame.display.set_caption("Digifiz Dashboard v" + digifiz_ver)

'''Create variables with image names we will use'''
background = pygame.image.load("images/background.png")
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
    screen.blit(speedtext, (820, 217))

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
    if rpmstate == 12:
        screen.blit(rpm200, (132, 4))




    #testing the illumination button

    if illuminationState == 0:
        screen.blit(illuminationOn, (45, 460))
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
