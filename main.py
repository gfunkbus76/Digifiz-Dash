"""
    Digifiz     v.03
    March 4th, 2021

    Attempting to code the Digifiz dash project cleaner
    Written by GFunkBus76 in 2021

    Opensource and designed from many online projects...
    Copy, paste, run, debug... repeat lol.

    Mainly inspired by ManxGauged and miata-dash on github.
    Redefined and cleaned up a bit.
    Use at your own discretion.

    Happy to help you if I can.

    https://github.com/gfunkbus76

"""


import pygame
from datetime import datetime
import paho.mqtt.client as mqttClient
from rpm.rpm import RpmGauge
from aux_gauge.AuxGauge import AuxGauge
from constants import *
from gauges import Gauge

#   Import pygame, for main graphics functions
#   Date time is for the clock and perhaps MQTT
#   Paho to handle the MQTT subscription from Node-Red


#   Currently enables RPM to rise and fall with keyboard up and down presses.
#   Will potentially change this in future to have full gauge functionality.
#   testingStatus = False

# Setup Display
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

# Title and Icon
programIcon = pygame.image.load(ICON)
pygame.display.set_icon(programIcon)

digifiz_ver = ".04 - March 4th"
pygame.display.set_caption("Digifiz Dashboard v" + digifiz_ver)

# Font Information
odo_font = pygame.font.Font(FONT_PATH, FONT_SMALL)
digital_font = pygame.font.Font(FONT_PATH, FONT_MEDIUM)
font_speedunits = pygame.font.Font(FONT_PATH, FONT_LARGE)

# Setup Game Loop
clock = pygame.time.Clock()

'''                        Game Variables                        '''

boost = AuxGauge(BOOST_XY, 19)
egt = AuxGauge(EGT_XY, 19)
coolant = AuxGauge(COOLANT_XY, 19)
oilpressure = AuxGauge(OILPRESSURE_XY, 19)
rpm = RpmGauge(RPM_XY, 50)

#   Gauge State Variables --> fed from local MQTT Server
rpm_status = 0
coolant_status = 0
egt_status = 0
oilpressure_status = 0
boost_status = 0
fuel_status = 0
outside_temp_status = 0
speed_status = 0



'''GPIO State Variables'''
#
# 0 is off, 1 is active -- Fed from the MQTT Server
illumination_state = 0
foglight_state = 0
highbeam_state = 0
defog_state = 0
leftturn_state = 0
rightturn_state = 0
brakewarn_state = 0
oillight_state = 0
alt_state = 0
glow_state = 0
fuelres_state = 0

# For the TestingStatus gauge change feature with the up/down arrows
gauge_change = 0

'''                         LOAD IMAGES                         '''

BACKGROUND = pygame.image.load(BG).convert_alpha()
MFA = pygame.image.load("images/indicators/MFA_temp.png").convert_alpha()
fuelresOn = pygame.image.load("images/indicators/fuelResOn.png").convert_alpha()
fuelresOff = pygame.image.load("images/indicators/fuelResOff.png").convert_alpha()


#   Creating the list for the indicator gauges
indicator_images = []
for i in range(10):
    image = pygame.image.load(("images/indicators/ind" + str(i) + ".png"))
    indicator_images.append(image)

######
#       MQTT Connection Function
######


def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


def on_message(client, userdata, message):
    print(message.topic + " " + message.payload.decode())


######
#       ENGINE TOPIC MQTT
######

def on_message_rpm(digi, obj, message):
    rpm_mqtt = int((message.payload.decode()))
    rpm.set_frame(rpm_mqtt)


def on_message_coolant(digi, obj, message):
    coolant_mqtt = int((message.payload.decode()))
    coolant.set_frame(coolant_mqtt)


def on_message_egt(digi, obj, message):
    egt_mqtt = int((message.payload.decode()))
    egt.set_frame(egt_mqtt)


def on_message_oilpressure(digi, obj, message):
    oilpressure_mqtt = int((message.payload.decode()))
    oilpressure.set_frame(oilpressure_mqtt)


def on_message_boost(digi, obj, message):
    boost_mqtt = int((message.payload.decode()))
    boost.set_frame(boost_mqtt)


######
#       CABIN TOPIC MQTT
######

def on_message_speed_cv(digi, obj, message):
    global speed_status
    global speed_cv_mqtt
    speed_cv_mqtt = int((message.payload.decode()))
    speed_status = speed_cv_mqtt


def on_message_speed_gps(digi, obj, message):
    global speed_gps_status
    global speed_gps_mqtt
    speed_gps_mqtt = int((message.payload.decode()))
    speed_gps_status = speed_gps_mqtt


def on_message_outside_temp(digi, obj, message):
    global outside_temp_status
    global outside_temp_mqtt
    outside_temp_mqtt = int((message.payload.decode()))
    outside_temp_status = outside_temp_mqtt


def on_message_fuel(digi, obj, message):
    global fuel_status
    global fuel_mqtt
    fuel_mqtt = int((message.payload.decode()))
    fuel_status = fuel_mqtt


######
#       INDICATOR TOPIC MQTT
######

def on_message_illumination(digi, obj, message):
    global illumination_state
    global illumination_mqtt
    illumination_mqtt = int((message.payload.decode()))
    illumination_state = illumination_mqtt


def on_message_foglight(digi, obj, message):
    global foglight_state
    global foglight_mqtt
    foglight_mqtt = int((message.payload.decode()))
    foglight_state = foglight_mqtt


def on_message_defog(digi, obj, message):
    global defog_state
    global defog_mqtt
    defog_mqtt = int((message.payload.decode()))
    defog_state = defog_mqtt


def on_message_highbeam(digi, obj, message):
    global highbeam_state
    global highbeam_mqtt
    highbeam_mqtt = int((message.payload.decode()))
    highbeam_state = highbeam_mqtt


def on_message_leftturn(digi, obj, message):
    global leftturn_state
    global leftturn_mqtt
    leftturn_mqtt = int((message.payload.decode()))
    leftturn_state = leftturn_mqtt


def on_message_rightturn(digi, obj, message):
    global rightturn_state
    global rightturn_mqtt
    rightturn_mqtt = int((message.payload.decode()))
    rightturn_state = rightturn_mqtt


def on_message_brakewarn(digi, obj, message):
    global brakewarn_state
    global brakewarn_mqtt
    brakewarn_mqtt = int((message.payload.decode()))
    brakewarn_state = brakewarn_mqtt


def on_message_oillight(digi, obj, message):
    global oillight_state
    global oillight_mqtt
    oillight_mqtt = int((message.payload.decode()))
    oillight_state = oillight_mqtt


def on_message_alt(digi, obj, message):
    global alt_state
    global alt_mqtt
    alt_mqtt = int((message.payload.decode()))
    alt_state = alt_mqtt


def on_message_glow(digi, obj, message):
    global glow_state
    global glow_mqtt
    glow_mqtt = int((message.payload.decode()))
    glow_state = glow_mqtt


######
#       Various Functions for Dash
######

def mileage():
    #   Text File or Odometer and Tripometer Information (pulled from ManxGauged project, just reads from text file
    #   Need to incorporate writing to the file after I figure out how to tabulate the mileage based on GPS or CV
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

#####
#       Functions for Drawing onto the screen
#####

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
    speedtext = font_speedunits.render(str(speed_status), True, NEON_YELLOW)
    text_rect = speedtext.get_rect()
    text_rect.midright = SPEEDO_XY
    WIN.blit(speedtext, text_rect)


def draw_clock_temp():
    global outside_temp_status
    now = datetime.now()
    WIN.blit(MFA, MFABG_XY)
    #   Draw MFA display
    text = digital_font.render(str(outside_temp_status), True, NEON_GREEN)
    #   Enables the text to be right center aligned
    text_rect = text.get_rect()
    text_rect.midright = MFA_XY
    WIN.blit(text, text_rect)

    bgclock_text = digital_font.render("00:00", True, DARK_GREY)
    WIN.blit(bgclock_text, CLOCK_XY)
    digital_text = now.strftime('%H:%M')
    text = digital_font.render(digital_text, True, NEON_GREEN)
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
    rpm.show(WIN)
    coolant.show(WIN)
    boost.show(WIN)
    oilpressure.show(WIN)
    egt.show(WIN)
    #WIN.blit(rpm_images[rpm_status], RPM_XY)
#    WIN.blit(aux_images[coolant_status], COOLANT_XY)
#    WIN.blit(aux_images[egt_status], EGT_XY)
#    WIN.blit(aux_images[oilpressure_status], OILPRESSURE_XY)
#    boost.show(WIN)
#    WIN.blit(aux_images[boost_status], BOOST_XY)



#####
#       Main Function for the Pygame Program
#####

def main():
    #   This was pulled off the internet from somewhere, adapted to work with my setup
    broker_address = "localhost"  # Broker address
    port = 1883  # Broker port

    client = mqttClient.Client("pytest")  # create new instance
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback

    client.connect(broker_address, port=port)  # connect to broker

    client.loop_start()  # start the loop
    run = True
    while run:
        clock.tick(FPS)
 #       global rpm_status   # for testing status below
#        global gauge_change # for testing status below
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Key up to change RPM based upon 'TestingStatus' state at top
        if testingStatus == True:
            if rpm_status == 50:
                gauge_change = False
            if rpm_status == 0:
                gauge_change = True
            if gauge_change:
                rpm_status + 1
            else:
                rpm_status - 1
        else:
            pass



        #   MQTT Stuff below
        client.subscribe("#") #     Subscribes to all topics
        client.message_callback_add('engine/rpm/state', on_message_rpm)
        client.message_callback_add('engine/egt/state', on_message_egt)
        client.message_callback_add('engine/oilpressure/state', on_message_oilpressure)
        client.message_callback_add('engine/boost/state', on_message_boost)
        client.message_callback_add('engine/coolant/state', on_message_coolant)
        client.message_callback_add('engine/fuel/state', on_message_fuel)
        client.message_callback_add('cabin/outside_temp/state', on_message_outside_temp)
        client.message_callback_add('cabin/speed_cv/state', on_message_speed_cv)
        client.message_callback_add('indicator/illumination/state', on_message_illumination)
        client.message_callback_add('indicator/foglight/state', on_message_foglight)
        client.message_callback_add('indicator/defog/state', on_message_defog)
        client.message_callback_add('indicator/highbeam/state', on_message_highbeam)
        client.message_callback_add('indicator/leftturn/state', on_message_leftturn)
        client.message_callback_add('indicator/rightturn/state', on_message_rightturn)
        client.message_callback_add('indicator/brakewarn/state', on_message_brakewarn)
        client.message_callback_add('indicator/oillight/state', on_message_oillight)
        client.message_callback_add('indicator/alt/state', on_message_alt)
        client.message_callback_add('indicator/glow/state', on_message_glow)

        draw_digifiz()
        mileage()
        draw_indicators()
        draw_clock_temp()
        draw_fuel_text()
        draw_speedometer_text()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
