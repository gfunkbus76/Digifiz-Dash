# Tech With Tim Tutorial

import pygame
from datetime import datetime

testingStatus = True

# Setup Display
pygame.init()
WIDTH, HEIGHT = 1920, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

# Colours
NEON_YELLOW = (236, 253, 147)
NEON_GREEN = (145, 213, 89)
DARK_GREY = (9, 52, 50)

# Title and Icon
programIcon = pygame.image.load('images/speedometer.png')
pygame.display.set_icon(programIcon)
digifiz_ver = ".03 - Feb 17"
pygame.display.set_caption("Digifiz Dashboard v" + digifiz_ver)

# Font Information
font_path = "fonts/DSEG7Classic-Bold.ttf"
FONT_LARGE = 174
FONT_MEDIUM = 94
digital_font = pygame.font.Font(font_path, FONT_MEDIUM)

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

rpm_status = 0
coolant_status = 0
egt_status = 0
oilpressure_status = 0
boost_status = 0
clock_status = 0

'''GPIO State Variables'''
# 0 is off, 1 is on
illumination_state  =       0
foglight_state      =       0
highbeam_state      =       0
defog_state         =       0
leftturn_state = 0
rightturn_state = 0
brakewarn_state = 0
oillight_state = 0
alt_state = 0
glow_state = 0
fuelres_state = 0
fuel_state = 6

'''Gauge State Data'''
speedHun = 1
speedTen = 4
speedOne = 2

gauge_change = 0


'''                         LOAD IMAGES                         '''

BACKGROUND = pygame.image.load("images/background.png")
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

def draw_clock():
    now = datetime.now()
    # draw digital clock
    bgclock_text = digital_font.render("00:00", True, DARK_GREY)
    WIN.blit(bgclock_text, CLOCK_XY)
    digital_text = now.strftime('%H:%M')
    text = digital_font.render(digital_text, True, NEON_YELLOW)
    WIN.blit(text, CLOCK_XY)
    pygame.display.update()

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

    if fuel_state <= 7:
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
        draw_indicators()
        draw_clock()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()