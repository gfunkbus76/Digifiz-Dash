# Tech With Tim Tutorial

import pygame
from datetime import datetime
import paho.mqtt.subscribe as subscribe


testingStatus = True

# Setup Display
pygame.init()
WIDTH, HEIGHT = 1920, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

# Colours
NEON_YELLOW = (236, 253, 147)
NEON_GREEN = (145, 213, 89)
DARK_GREY = (9, 52, 50)
RED = (255, 0, 0)

# Title and Icon
programIcon = pygame.image.load('images/speedometer.png')
pygame.display.set_icon(programIcon)
digifiz_ver = ".03 - Feb 19th"
pygame.display.set_caption("Digifiz Dashboard v" + digifiz_ver)

# Font Information
FONT_PATH = "fonts/DSEG7Classic-Bold.ttf"
FONT_LARGE = 174
FONT_MEDIUM = 94
FONT_SMALL = 67
odo_font = pygame.font.Font(FONT_PATH, FONT_SMALL)
digital_font = pygame.font.Font(FONT_PATH, FONT_MEDIUM)
font_speedunits = pygame.font.Font(FONT_PATH, FONT_LARGE)

# Setup Game Loop
FPS = 60
clock = pygame.time.Clock()

'''                        Game Variables                        '''
#   Locations
RPM_XY = (135, 5)
COOLANT_XY = (1481, 105)
EGT_XY = (1599, 105)
OILPRESSURE_XY = (1711, 105)
BOOST_XY = (1822, 105)
CLOCK_XY = (555, 620)
FUEL_XY = (1560, 620)
ODO_XY = (60, 644)
ODO_L_XY = (395,678)
MFA_XY = (1435, 668)
MFABG_XY = (1021, 563)
SPEEDO_XY = (1247, 305)


#   Gauge State Variables --> need to feed from arduino data
rpm_status = 0
coolant_status = 5
egt_status = 5
oilpressure_status = 10
boost_status = 12
fuel_status = 4
outside_temp_status = 22
speed_status = 8

#   Odometer / Tripmeter Data


'''GPIO State Variables'''
# 0 is off, 1 is on
illumination_state = 0
foglight_state = 0
highbeam_state = 0
defog_state = 1
leftturn_state = 0
rightturn_state = 0
brakewarn_state = 0
oillight_state = 1
alt_state = 0
glow_state = 0
fuelres_state = 0

gauge_change = 0


'''                         LOAD IMAGES                         '''

BACKGROUND = pygame.image.load("images/background.png").convert_alpha()
MFA = pygame.image.load("images/indicators/MFA_temp.png").convert_alpha()
fuelresOn = pygame.image.load("images/indicators/fuelResOn.png").convert_alpha()
fuelresOff = pygame.image.load("images/indicators/fuelResOff.png").convert_alpha()

rpm_images = []
for i in range(51):
    image = pygame.image.load("images/rpm/RPM " + str(i) + "00.png")
    rpm_images.append(image)

aux_images = []
for i in range(20):
    image = pygame.image.load("images/gauges/aux" + str(i) + ".png")
    aux_images.append(image)

indicator_images = []
for i in range(10):
    image = pygame.image.load(("images/indicators/ind" + str(i) + ".png"))
    indicator_images.append(image)


def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))


def mileage():
    #   Text File or Odometer and Tripometer Information
    global odo_font
    odometer = 0
    tripometer = 0
    odofile = open("odo.txt", "r")
    odo_from_file_text_line1 = odofile.readline()
    response = odo_from_file_text_line1.replace('\n', "")
    response2 = response.replace('\r', "")
    response3 = response2.replace("odo:", "")
    try:
        odometer = int(response3)
    except:
        print("Error: ODO read from file is not an int")
        error_reading_odo_from_file = 1
    odometer_arduino = odometer

    odo_from_file_text_line2 = odofile.readline()
    response = odo_from_file_text_line2.replace('\n', "")
    response2 = response.replace('\r', "")
    response3 = response2.replace("trip:", "")
    try:
        tripometer = int(response3)
    except:
        print
        "Error: Trip read from file is not an int"
        error_reading_odo_from_file = 1
    odofile.close()


    digital_odo = odometer
    odo_text = odo_font.render(str(digital_odo), True, NEON_GREEN)
    text_rect = odo_text.get_rect()
    text_rect.midright = ODO_L_XY
    WIN.blit(odo_text, text_rect)



def draw_fuel_text():
    global digital_font
    digital_fuel = fuel_status
    fuel_text = digital_font.render(str(int(digital_fuel)), True, NEON_GREEN)
    text_rect = fuel_text.get_rect()
    text_rect.midright = 1717, 667
    WIN.blit(fuel_text, text_rect)

def draw_speedometer_text():
    ''' Speedometer Font Testing '''
    global speed_status
    global font_speedunits
    speedtext = font_speedunits.render(str(speed_status), 1, NEON_YELLOW)
    text_rect = speedtext.get_rect()
    text_rect.midright = SPEEDO_XY
    WIN.blit(speedtext, text_rect)


def draw_clock_temp():
    global outside_temp_status
    now = datetime.now()
    WIN.blit(MFA, MFABG_XY)
    #   Draw MFA display
    text = digital_font.render(str(outside_temp_status), 1, NEON_GREEN)
    #   Enables the text to be right center aligned
    text_rect = text.get_rect()
    text_rect.midright = MFA_XY
    WIN.blit(text, text_rect)

    bgclock_text = digital_font.render("00:00", 1, DARK_GREY)
    WIN.blit(bgclock_text, CLOCK_XY)
    digital_text = now.strftime('%H:%M')
    text = digital_font.render(digital_text, 1, NEON_GREEN)
    WIN.blit(text, CLOCK_XY)


def draw_indicators():
    if illumination_state == 1:
        WIN.blit(indicator_images[0], (45, 460))
    if foglight_state == 1:
        WIN.blit(indicator_images[1], (185, 460))
    if defog_state == 1:
        WIN.blit(indicator_images[2], (325, 460))
    if highbeam_state == 1:
        WIN.blit(indicator_images[3], (465, 460))
    if leftturn_state == 1:
        WIN.blit(indicator_images[4], (605, 460))
    if rightturn_state == 1:
        WIN.blit(indicator_images[5], (1220, 460))
    if brakewarn_state == 1:
        WIN.blit(indicator_images[6], (1360, 460))
    if oillight_state == 1:
        WIN.blit(indicator_images[7], (1500, 460))
    if alt_state == 1:
        WIN.blit(indicator_images[8], (1640, 460))
    if glow_state == 1:
        WIN.blit(indicator_images[9], (1780, 460))

    if fuel_status <= 7:
        WIN.blit(fuelresOn, (1795, 616))
    else:
        WIN.blit(fuelresOff, (1795, 616))


def draw_digifiz():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(rpm_images[rpm_status], RPM_XY)
    WIN.blit(aux_images[coolant_status], COOLANT_XY)
    WIN.blit(aux_images[egt_status], EGT_XY)
    WIN.blit(aux_images[oilpressure_status], OILPRESSURE_XY)
    WIN.blit(aux_images[boost_status], BOOST_XY)


def active_dash():
    pass


def main():

    run = True
    while run:
        clock.tick(FPS)
        global rpm_status
        global gauge_change
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Key up to change RPM
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if rpm_status <= 50:
                    gauge_change = +1
                if rpm_status == 50:
                    gauge_change = 0
            if event.key == pygame.K_DOWN:
                if rpm_status <= 50:
                    gauge_change = -1
                if rpm_status == 0:
                    gauge_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                gauge_change = 0
            if event.key == pygame.K_DOWN:
                gauge_change = 0

        rpm_status += gauge_change
        draw_digifiz()
        mileage()
        draw_indicators()
        draw_clock_temp()
        draw_fuel_text()
        draw_speedometer_text()
        pygame.display.update()
        subscribe.callback(on_message_print, "engine/egt/state", hostname="localhost")

    pygame.quit()


if __name__ == "__main__":
    main()
