import sys, os, time

# import RPi.GPIO as GPIO
# from pygame import Surface
# from pygame.surface import SurfaceType

'''import constants used by pygame such as event type = QUIT'''
import pygame.locals
from datetime import datetime
from threading import Event

from pygame.locals import *

testingStatus = True

'''Vehicle Information'''
vehicle_owner = "Gavin"
digifiz_ver = "0.1"
number_points_speedsensor = 2
wheelcircumference = 0.000378788  # miles

'''Screen Size and font colours'''
size = (1920, 720)

path_to_folder = "~/Users/Gavin/Documents/Digifiz-Dash/"

'''fuel xy'''
fuelX = 1557
fuelY = 621

'''GPIO State Variables'''
# 0 is off, 1 is on
illuminationState = 1
foglightState = 0
highbeamState = 0
defogState = 0
leftturnState = 0
rightturnState = 0
brakewarnState = 0
oillightState = 1
altState = 0
glowState = 1
fuelresState = 1
fuelState = 10

'''Arduino Data'''
fuel_level_adc_arduino = "0"

'''Gauge State Data'''
rpmState = 2
coolantState = 1
egtState = 2
oilPressureState = 3
boostState = 4
clockState = 0
speedHun = 1
speedTen = 4
speedOne = 2


delay = 1 # attempting to delay a loop
direction = 1  # will be 1 for climbing, -1 for falling
sweepStatus = 0

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)

'''Pygame Icon'''
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

'''Used to manage how fast the screen updates'''
clock = pygame.time.Clock()
fps = 30

'''Create variables with image names we will use'''
background = pygame.image.load("images/background.png")
illuminationOn = pygame.image.load("images/illuminationOn.png").convert_alpha()
illuminationOff = pygame.image.load("images/illuminationOff.png").convert_alpha()
foglightOn = pygame.image.load("images/foglightOn.png").convert_alpha()
foglightOff = pygame.image.load("images/foglightOff.png").convert_alpha()
defogOn = pygame.image.load("images/defogOn.png").convert_alpha()
defogOff = pygame.image.load("images/defogOff.png").convert_alpha()
highbeamOn = pygame.image.load("images/highbeamOn.png").convert_alpha()
highbeamOff = pygame.image.load("images/highbeamOff.png").convert_alpha()
leftturnOn = pygame.image.load("images/leftturnOn.png").convert_alpha()
leftturnOff = pygame.image.load("images/leftturnOff.png").convert_alpha()
rightturnOn = pygame.image.load("images/rightturnOn.png").convert_alpha()
rightturnOff = pygame.image.load("images/rightturnOff.png").convert_alpha()
oillightOn = pygame.image.load("images/oillightOn.png").convert_alpha()
oillightOff = pygame.image.load("images/oillightOff.png").convert_alpha()
glowOn = pygame.image.load("images/glowOn.png").convert_alpha()
glowOff = pygame.image.load("images/glowOff.png").convert_alpha()
altOn = pygame.image.load("images/altOn.png").convert_alpha()
altOff = pygame.image.load("images/altOff.png").convert_alpha()
brakewarnOn = pygame.image.load("images/brakewarnOn.png").convert_alpha()
brakewarnOff = pygame.image.load("images/brakewarnOff.png").convert_alpha()
fuelresOn = pygame.image.load("images/fuelResOn.png").convert_alpha()
fuelresOff = pygame.image.load("images/fuelResOff.png").convert_alpha()

'''RPM VARIABLES'''
rpm000 = pygame.image.load("images/RPM 000.png").convert_alpha()
rpm100 = pygame.image.load("images/RPM 100.png").convert_alpha()
rpm200 = pygame.image.load("images/RPM 200.png").convert_alpha()
rpm300 = pygame.image.load("images/RPM 300.png").convert_alpha()
rpm400 = pygame.image.load("images/RPM 400.png").convert_alpha()
rpm500 = pygame.image.load("images/RPM 500.png").convert_alpha()
rpm600 = pygame.image.load("images/RPM 600.png").convert_alpha()
rpm700 = pygame.image.load("images/RPM 700.png").convert_alpha()
rpm800 = pygame.image.load("images/RPM 800.png").convert_alpha()
rpm900 = pygame.image.load("images/RPM 900.png").convert_alpha()
rpm1000 = pygame.image.load("images/RPM 1000.png").convert_alpha()
rpm1100 = pygame.image.load("images/RPM 1100.png").convert_alpha()
rpm1200 = pygame.image.load("images/RPM 1200.png").convert_alpha()
rpm1300 = pygame.image.load("images/RPM 1300.png").convert_alpha()
rpm1400 = pygame.image.load("images/RPM 1400.png").convert_alpha()
rpm1500 = pygame.image.load("images/RPM 1500.png").convert_alpha()
rpm1600 = pygame.image.load("images/RPM 1600.png").convert_alpha()
rpm1700 = pygame.image.load("images/RPM 1700.png").convert_alpha()
rpm1800 = pygame.image.load("images/RPM 1800.png").convert_alpha()
rpm1900 = pygame.image.load("images/RPM 1900.png").convert_alpha()
rpm2000 = pygame.image.load("images/RPM 2000.png").convert_alpha()
rpm2100 = pygame.image.load("images/RPM 2100.png").convert_alpha()
rpm2200 = pygame.image.load("images/RPM 2200.png").convert_alpha()
rpm2300 = pygame.image.load("images/RPM 2300.png").convert_alpha()
rpm2400 = pygame.image.load("images/RPM 2400.png").convert_alpha()
rpm2500 = pygame.image.load("images/RPM 2500.png").convert_alpha()
rpm2600 = pygame.image.load("images/RPM 2600.png").convert_alpha()
rpm2700 = pygame.image.load("images/RPM 2700.png").convert_alpha()
rpm2800 = pygame.image.load("images/RPM 2800.png").convert_alpha()
rpm2900 = pygame.image.load("images/RPM 2900.png").convert_alpha()
rpm3000 = pygame.image.load("images/RPM 3000.png").convert_alpha()
rpm3100 = pygame.image.load("images/RPM 3100.png").convert_alpha()
rpm3200 = pygame.image.load("images/RPM 3200.png").convert_alpha()
rpm3300 = pygame.image.load("images/RPM 3300.png").convert_alpha()
rpm3400 = pygame.image.load("images/RPM 3400.png").convert_alpha()
rpm3500 = pygame.image.load("images/RPM 3500.png").convert_alpha()
rpm3600 = pygame.image.load("images/RPM 3600.png").convert_alpha()
rpm3700 = pygame.image.load("images/RPM 3700.png").convert_alpha()
rpm3800 = pygame.image.load("images/RPM 3800.png").convert_alpha()
rpm3900 = pygame.image.load("images/RPM 3900.png").convert_alpha()
rpm4000 = pygame.image.load("images/RPM 4000.png").convert_alpha()
rpm4100 = pygame.image.load("images/RPM 4100.png").convert_alpha()
rpm4200 = pygame.image.load("images/RPM 4200.png").convert_alpha()
rpm4300 = pygame.image.load("images/RPM 4300.png").convert_alpha()
rpm4400 = pygame.image.load("images/RPM 4400.png").convert_alpha()
rpm4500 = pygame.image.load("images/RPM 4500.png").convert_alpha()
rpm4600 = pygame.image.load("images/RPM 4600.png").convert_alpha()
rpm4700 = pygame.image.load("images/RPM 4700.png").convert_alpha()
rpm4800 = pygame.image.load("images/RPM 4800.png").convert_alpha()
rpm4900 = pygame.image.load("images/RPM 4900.png").convert_alpha()
rpm5000 = pygame.image.load("images/RPM 5000.png").convert_alpha()

'''Aux Images'''
aux19 = pygame.image.load("images/aux19.png").convert_alpha()
aux18 = pygame.image.load("images/aux18.png").convert_alpha()
aux17 = pygame.image.load("images/aux17.png").convert_alpha()
aux16 = pygame.image.load("images/aux16.png").convert_alpha()
aux15 = pygame.image.load("images/aux15.png").convert_alpha()
aux14 = pygame.image.load("images/aux14.png").convert_alpha()
aux13 = pygame.image.load("images/aux13.png").convert_alpha()
aux12 = pygame.image.load("images/aux12.png").convert_alpha()
aux11 = pygame.image.load("images/aux11.png").convert_alpha()
aux10 = pygame.image.load("images/aux10.png").convert_alpha()
aux09 = pygame.image.load("images/aux09.png").convert_alpha()
aux08 = pygame.image.load("images/aux08.png").convert_alpha()
aux07 = pygame.image.load("images/aux07.png").convert_alpha()
aux06 = pygame.image.load("images/aux06.png").convert_alpha()
aux05 = pygame.image.load("images/aux05.png").convert_alpha()
aux04 = pygame.image.load("images/aux04.png").convert_alpha()
aux03 = pygame.image.load("images/aux03.png").convert_alpha()
aux02 = pygame.image.load("images/aux02.png").convert_alpha()
aux01 = pygame.image.load("images/aux01.png").convert_alpha()
aux00 = pygame.image.load("images/aux00.png").convert_alpha()

'''Display Font'''
font_path = "fonts/DSEG7Classic-Bold.ttf"
font_size = 174
fontObj = pygame.font.Font(font_path, font_size)
indHL = (236, 253, 147)
bgColour = (9, 52, 50)
fuelHL = (145, 213, 89)

'''Clock Stuffs'''
font_lower_size = 94
clockX = 555
clockY = 620
digital_font = pygame.font.Font(font_path, font_lower_size)

# Main Loop
running = True
while running:
    pygame.display.flip()
    '''The code below quits the program if the X button is pressed'''
    for event in pygame.event.get():
        if event.type == QUIT:
            #   ser.close()
            pygame.quit()
            sys.exit()

    '''Now we have initialized everything, lets start with the main part'''

    # Background image
    screen.blit(background, (0, 0))
    now = datetime.now()

    ''' Speedometer Font Testing '''
    # Speed in hundreds
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render(str(speedHun), 1, indHL)
    # speedtext_rect = speedtext.get_rect()
    # speedtext_rect.right = 435
    # screen.blit(speedtext, (828,217), speedtext_rect)
    screen.blit(speedtext, (820, 217))

    # Speed in tens
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render(str(speedTen), 0, indHL)
    screen.blit(speedtext, (962, 217))

    # Speed in singles
    font_speedunits = pygame.font.Font(font_path, font_size)
    speedtext = font_speedunits.render(str(speedOne), 0, indHL)
    screen.blit(speedtext, (1104, 217))
    # pygame.display.flip()

    ''' RPM '''
    if rpmState == 50:
        screen.blit(rpm5000, (135, 5))
    elif rpmState == 49:
        screen.blit(rpm4900, (135, 5))
    elif rpmState == 48:
        screen.blit(rpm4800, (135, 5))
    elif rpmState == 47:
        screen.blit(rpm4700, (135, 5))
    elif rpmState == 46:
        screen.blit(rpm4600, (135, 5))
    elif rpmState == 45:
        screen.blit(rpm4500, (135, 5))
    elif rpmState == 44:
        screen.blit(rpm4400, (135, 5))
    elif rpmState == 43:
        screen.blit(rpm4300, (135, 5))
    elif rpmState == 42:
        screen.blit(rpm4200, (135, 5))
    elif rpmState == 41:
        screen.blit(rpm4100, (135, 5))
    elif rpmState == 40:
        screen.blit(rpm4000, (135, 5))
    elif rpmState == 39:
        screen.blit(rpm3900, (135, 5))
    elif rpmState == 38:
        screen.blit(rpm3800, (135, 5))
    elif rpmState == 37:
        screen.blit(rpm3700, (135, 5))
    elif rpmState == 36:
        screen.blit(rpm3600, (135, 5))
    elif rpmState == 35:
        screen.blit(rpm3500, (135, 5))
    elif rpmState == 34:
        screen.blit(rpm3400, (135, 5))
    elif rpmState == 33:
        screen.blit(rpm3300, (135, 5))
    elif rpmState == 32:
        screen.blit(rpm3200, (135, 5))
    elif rpmState == 31:
        screen.blit(rpm3100, (135, 5))
    elif rpmState == 30:
        screen.blit(rpm3000, (135, 5))
    elif rpmState == 29:
        screen.blit(rpm2900, (135, 5))
    elif rpmState == 28:
        screen.blit(rpm2800, (135, 5))
    elif rpmState == 27:
        screen.blit(rpm2700, (135, 5))
    elif rpmState == 26:
        screen.blit(rpm2600, (135, 5))
    elif rpmState == 25:
        screen.blit(rpm2500, (135, 5))
    elif rpmState == 24:
        screen.blit(rpm2400, (135, 5))
    elif rpmState == 23:
        screen.blit(rpm2300, (135, 5))
    elif rpmState == 22:
        screen.blit(rpm2200, (135, 5))
    elif rpmState == 21:
        screen.blit(rpm2100, (135, 5))
    elif rpmState == 20:
        screen.blit(rpm2000, (135, 5))
    elif rpmState == 19:
        screen.blit(rpm1900, (135, 5))
    elif rpmState == 18:
        screen.blit(rpm1800, (135, 5))
    elif rpmState == 17:
        screen.blit(rpm1700, (135, 5))
    elif rpmState == 16:
        screen.blit(rpm1600, (135, 5))
    elif rpmState == 15:
        screen.blit(rpm1500, (135, 5))
    elif rpmState == 14:
        screen.blit(rpm1400, (135, 5))
    elif rpmState == 13:
        screen.blit(rpm1300, (135, 5))
    elif rpmState == 12:
        screen.blit(rpm1200, (135, 5))
    elif rpmState == 11:
        screen.blit(rpm1100, (135, 5))
    elif rpmState == 10:
        screen.blit(rpm1000, (135, 5))
    elif rpmState == 9:
        screen.blit(rpm900, (135, 5))
    elif rpmState == 8:
        screen.blit(rpm800, (135, 5))
    elif rpmState == 7:
        screen.blit(rpm700, (135, 5))
    elif rpmState == 6:
        screen.blit(rpm600, (135, 5))
    elif rpmState == 5:
        screen.blit(rpm500, (135, 5))
    elif rpmState == 4:
        screen.blit(rpm400, (135, 5))
    elif rpmState == 3:
        screen.blit(rpm300, (135, 5))
    elif rpmState == 2:
        screen.blit(rpm200, (135, 5))
    elif rpmState == 1:
        screen.blit(rpm100, (135, 5))
    elif rpmState == 0:
        screen.blit(rpm000, (135, 5))

    '''Coolant Gauge graphics'''
    if coolantState == 19:
        screen.blit(aux19, (1481, 105))
    elif coolantState == 18:
        screen.blit(aux18, (1481, 105))
    elif coolantState == 17:
        screen.blit(aux17, (1481, 105))
    elif coolantState == 16:
        screen.blit(aux16, (1481, 105))
    elif coolantState == 15:
        screen.blit(aux15, (1481, 105))
    elif coolantState == 14:
        screen.blit(aux14, (1481, 105))
    elif coolantState == 13:
        screen.blit(aux13, (1481, 105))
    elif coolantState == 12:
        screen.blit(aux12, (1481, 105))
    elif coolantState == 11:
        screen.blit(aux11, (1481, 105))
    elif coolantState == 10:
        screen.blit(aux10, (1481, 105))
    elif coolantState == 9:
        screen.blit(aux09, (1481, 105))
    elif coolantState == 8:
        screen.blit(aux08, (1481, 105))
    elif coolantState == 7:
        screen.blit(aux07, (1481, 105))
    elif coolantState == 6:
        screen.blit(aux06, (1481, 105))
    elif coolantState == 5:
        screen.blit(aux05, (1481, 105))
    elif coolantState == 4:
        screen.blit(aux04, (1481, 105))
    elif coolantState == 3:
        screen.blit(aux03, (1481, 105))
    elif coolantState == 2:
        screen.blit(aux02, (1481, 105))
    elif coolantState == 1:
        screen.blit(aux01, (1481, 105))
    elif coolantState == 0:
        screen.blit(aux00, (1481, 105))

    '''EGT Gauge'''
    if egtState == 19:
        screen.blit(aux19, (1599, 105))
    elif egtState == 18:
        screen.blit(aux18, (1599, 105))
    elif egtState == 17:
        screen.blit(aux17, (1599, 105))
    elif egtState == 16:
        screen.blit(aux16, (1599, 105))
    elif egtState == 15:
        screen.blit(aux15, (1599, 105))
    elif egtState == 14:
        screen.blit(aux14, (1599, 105))
    elif egtState == 13:
        screen.blit(aux13, (1599, 105))
    elif egtState == 12:
        screen.blit(aux12, (1599, 105))
    elif egtState == 11:
        screen.blit(aux11, (1599, 105))
    elif egtState == 18:
        screen.blit(aux18, (1599, 105))
    elif egtState == 9:
        screen.blit(aux09, (1599, 105))
    elif egtState == 8:
        screen.blit(aux08, (1599, 105))
    elif egtState == 7:
        screen.blit(aux07, (1599, 105))
    elif egtState == 6:
        screen.blit(aux06, (1599, 105))
    elif egtState == 5:
        screen.blit(aux05, (1599, 105))
    elif egtState == 4:
        screen.blit(aux04, (1599, 105))
    elif egtState == 3:
        screen.blit(aux03, (1599, 105))
    elif egtState == 2:
        screen.blit(aux02, (1599, 105))
    elif egtState == 1:
        screen.blit(aux01, (1599, 105))
    elif egtState == 0:
        screen.blit(aux00, (1599, 105))

    '''Oil Pressure Gauge'''
    if oilPressureState == 19:
        screen.blit(aux19, (1711, 105))
    elif oilPressureState == 18:
        screen.blit(aux18, (1711, 105))
    elif oilPressureState == 17:
        screen.blit(aux17, (1711, 105))
    elif oilPressureState == 16:
        screen.blit(aux16, (1711, 105))
    elif oilPressureState == 15:
        screen.blit(aux15, (1711, 105))
    elif oilPressureState == 14:
        screen.blit(aux14, (1711, 105))
    elif oilPressureState == 13:
        screen.blit(aux13, (1711, 105))
    elif oilPressureState == 12:
        screen.blit(aux12, (1711, 105))
    elif oilPressureState == 11:
        screen.blit(aux11, (1711, 105))
    elif oilPressureState == 18:
        screen.blit(aux18, (1711, 105))
    elif oilPressureState == 9:
        screen.blit(aux09, (1711, 105))
    elif oilPressureState == 8:
        screen.blit(aux08, (1711, 105))
    elif oilPressureState == 7:
        screen.blit(aux07, (1711, 105))
    elif oilPressureState == 6:
        screen.blit(aux06, (1711, 105))
    elif oilPressureState == 5:
        screen.blit(aux05, (1711, 105))
    elif oilPressureState == 4:
        screen.blit(aux04, (1711, 105))
    elif oilPressureState == 3:
        screen.blit(aux03, (1711, 105))
    elif oilPressureState == 2:
        screen.blit(aux02, (1711, 105))
    elif oilPressureState == 1:
        screen.blit(aux01, (1711, 105))
    elif oilPressureState == 0:
        screen.blit(aux00, (1711, 105))

    '''Boost Gauge'''
    if boostState == 19:
        screen.blit(aux19, (1822, 105))
    elif boostState == 18:
        screen.blit(aux18, (1822, 105))
    elif boostState == 17:
        screen.blit(aux17, (1822, 105))
    elif boostState == 16:
        screen.blit(aux16, (1822, 105))
    elif boostState == 15:
        screen.blit(aux15, (1822, 105))
    elif boostState == 14:
        screen.blit(aux14, (1822, 105))
    elif boostState == 13:
        screen.blit(aux13, (1822, 105))
    elif boostState == 12:
        screen.blit(aux12, (1822, 105))
    elif boostState == 11:
        screen.blit(aux11, (1822, 105))
    elif boostState == 18:
        screen.blit(aux18, (1822, 105))
    elif boostState == 9:
        screen.blit(aux09, (1822, 105))
    elif boostState == 8:
        screen.blit(aux08, (1822, 105))
    elif boostState == 7:
        screen.blit(aux07, (1822, 105))
    elif boostState == 6:
        screen.blit(aux06, (1822, 105))
    elif boostState == 5:
        screen.blit(aux05, (1822, 105))
    elif boostState == 4:
        screen.blit(aux04, (1822, 105))
    elif boostState == 3:
        screen.blit(aux03, (1822, 105))
    elif boostState == 2:
        screen.blit(aux02, (1822, 105))
    elif boostState == 1:
        screen.blit(aux01, (1822, 105))
    elif boostState == 0:
        screen.blit(aux00, (1822, 105))

    '''Dash GPIO Activated Indicators aka Dummy Lights etc'''

    if illuminationState == 0:
        screen.blit(illuminationOff, (45, 460))
    #   GPIO.output(lightbarpin, False)
    else:
        screen.blit(illuminationOn, (45, 460))
    #   GPIO.output(lightbarpin, True)
    #   pygame.display.update()

    if foglightState == 0:
        screen.blit(foglightOff, (185, 460))
    else:
        screen.blit(foglightOn, (185, 460))

    if defogState == 0:
        screen.blit(defogOff, (325, 460))
    else:
        screen.blit(foglightOn, (325, 460))

    if highbeamState == 0:
        screen.blit(highbeamOff, (465, 460))
    else:
        screen.blit(highbeamOn, (465, 460))

    if leftturnState == 0:
        screen.blit(leftturnOff, (605, 460))
    else:
        screen.blit(leftturnOn, (605, 460))

    if rightturnState == 0:
        screen.blit(rightturnOff, (1220, 460))
    else:
        continue

    if brakewarnState == 0:
        screen.blit(brakewarnOff, (1360, 460))
    else:
        screen.blit(brakewarnOn, (1360, 460))

    if oillightState == 0:
        screen.blit(oillightOff, (1500, 460))
    else:
        screen.blit(oillightOn, (1500, 460))

    if altState == 0:
        screen.blit(altOff, (1640, 460))
    else:
        screen.blit(altOn, (1640, 460))

    if glowState == 0:
        screen.blit(glowOff, (1780, 460))
    else:
        screen.blit(glowOn, (1780, 460))

    ''' Fuel Gauge Stuffs'''
    #    if fuelresState == 0:
    if fuelState <= 7:
        screen.blit(fuelresOn, (1795, 616))
    else:
        screen.blit(fuelresOff, (1795, 616))

    clock.tick(fps)

    '''
    def testing_status(gauge):
    gauge += direction
    if gauge == 50:
        direction = -1
    elif gauge == 0:
        direction = 1 
    '''

    if testingStatus:
        rpmState += direction # always move, in whichever direction

        # figure out if you need to change direction
        # Note that these ifs simply won't trigger until it's time to
        # change.
        if rpmState == 50:
            direction = -1
        elif rpmState == 0:
            direction = 1
        #elif
        #    direction = 0


#        egtState += direction
#        if egtState == 19:
#            direction = -1
#        elif egtState == 1:
#            direction = 1
#        if rpmState < 19:
#            rpmState += 1
#        else:
#            rpmState = 0

        if egtState < 19:
            egtState += 1
        else:
            egtState = 0


        if boostState < 19:
            boostState += 1
        else:
            boostState = 0

        if coolantState < 19:
            coolantState += 1
        else:
            coolantState = 0

        if oilPressureState < 19:
            oilPressureState += 1
        else:
            oilPressureState = 0

        if speedTen < 9:
#            pygame.time.wait(500)
            speedTen += 1
        else:
            speedTen = 0

        if speedOne < 9:
            speedOne += 1
        else:
            speedOne = 0

        if fuelState >= 70:
            fuelState -= 1


   # rpmState = 50

   # if testingStatus == 1:
   #     if rpmState > 50:
    #    rpmState -= 1

#    if testingStatus == 1:
#        if rpmState < 50:
#            rpmState += 1
#        elif rpmState > 0:
#            rpmState = 0



   # rpmState = 0
    #    if rpmState > 50: rpmState = 0
    #        if rpmState == 50:
    #           rpmState == 0

    '''Calculate  Fuel Level'''
    '''fuel_level_adc_arduino = "0" #note: this value from pi is a raw dump of the adc from 0 to 1024 (630=emplty, 210=full) '''
    try:
        eqn_m = (0.0 - 100.0) / (630.0 - 165.0)
        eqn_b = 100.0 - (eqn_m * 165.0)
        fuel_level = (float(fuel_level_adc_arduino) * eqn_m) + eqn_b
        fuelstate = int((fuel_level / 100) * 16)
    # print "ardu:"+fuel_level_adc_arduino+"fuel100:"+str(fuel_level)+"m:"+str(eqn_m)+"b:"+str(eqn_b)
    except:
        print
        "error fuel level"

    '''Fuel Gauge'''
    digital_fuel = fuelState
    fuel_text = digital_font.render(str(int(digital_fuel)), True, fuelHL)
    screen.blit(fuel_text, (fuelX, fuelY))



    '''Clock Stuffs'''
    # draw digital clock
    bgclock_text = digital_font.render("00:00", True, bgColour)
    screen.blit(bgclock_text, (clockX, clockY))
    digital_text = now.strftime('%H:%M')
    text = digital_font.render(digital_text, True, indHL)
    screen.blit(text, (clockX, clockY))

    pygame.display.update()
