# Tech With Tim Tutorial

import pygame
from datetime import datetime
import paho.mqtt.client as mqttClient
import time


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
coolant_status = 0
egt_status = 0
oilpressure_status = 0
boost_status = 0
fuel_status = 0
outside_temp_status = 0
speed_status = 0

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

def on_message_rpm(mosq, obj, message):
    #print(str(message.payload.decode())[0:6])
    global rpm_status
    global rpm_mqtt
    rpm_mqtt = int((message.payload.decode())[0:6])
    rpm_status = rpm_mqtt

def on_message_coolant(mosq, obj, message):
    #egt_status = (str(message.payload.decode())[0:5])
    global coolant_status
    global coolant_mqtt
    coolant_mqtt = int((message.payload.decode())[0:6])
    coolant_status = coolant_mqtt

def on_message_egt(mosq, obj, message):
    #egt_status = (str(message.payload.decode())[0:5])
    global egt_status
    global egt_mqtt
    egt_mqtt = int((message.payload.decode())[0:6])
    egt_status = egt_mqtt

def on_message_oilpressure(mosq, obj, message):
    #egt_status = (str(message.payload.decode())[0:5])
    global oilpressure_status
    global oilpressure_mqtt
    oilpressure_mqtt = int((message.payload.decode())[0:6])
    oilpressure_status = oilpressure_mqtt

def on_message_boost(mosq, obj, message):
    #print(str(message.payload.decode())[0:6])
    global boost_status
    global boost_mqtt
    boost_mqtt = int((message.payload.decode())[0:6])
    boost_status = boost_mqtt

######
#       CABIN TOPIC MQTT
######

def on_message_speed_cv(mosq, obj, message):
    global speed_status
    global speed_cv_mqtt
    speed_cv_mqtt = int((message.payload.decode())[0:6])
    speed_status = speed_cv_mqtt

def on_message_speed_gps(mosq, obj, message):
    global speed_gps_status
    global speed_gps_mqtt
    speed_gps_mqtt = int((message.payload.decode())[0:6])
    speed_gps_status = speed_gps_mqtt

def on_message_outside_temp(mosq, obj, message):
    global outside_temp_status
    global outside_temp_mqtt
    outside_temp_mqtt = int((message.payload.decode())[0:6])
    outside_temp_status = outside_temp_mqtt

def on_message_fuel(mosq, obj, message):
    global fuel_status
    global fuel_mqtt
    fuel_mqtt = int((message.payload.decode())[0:6])
    fuel_status = fuel_mqtt

def on_message_speed_cv(mosq, obj, message):
    global speed_status
    global speed_cv_mqtt
    speed_cv_mqtt = int((message.payload.decode())[0:6])
    speed_status = speed_cv_mqtt

def on_message_speed_gps(mosq, obj, message):
    global speed_gps_status
    global speed_gps_mqtt
    speed_gps_mqtt = int((message.payload.decode())[0:6])
    speed_gps_status = speed_gps_mqtt
'''
class indicators()
    pass

    illumination_state
    foglight_state
    defog_state
    highbeam_state
    leftturn_state
    rightturn_state
    brakewarn_state
    oillight_state
    alt_state
    glow_state
    fuel_status
'''



######
#       Varios Functions for Dash
######

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


def mqtt_stuff():
    pass

def main():
    broker_address = "localhost"  # Broker address
    port = 1883  # Broker port

    client = mqttClient.Client("pytest")  # create new instance
    # client.username_pw_set(user, password=password)  # set username and password
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback

    client.connect(broker_address, port=port)  # connect to broker

    client.loop_start()  # start the loop
    run = True
    while run:
        clock.tick(FPS)
        global rpm_status
        global gauge_change
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Key up to change RPM
        if testingStatus == True:
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
#        rpm_status = on_message_rpm(mosq, obj, messge)
        draw_digifiz()
        mileage()
        draw_indicators()
        draw_clock_temp()
        draw_fuel_text()
        draw_speedometer_text()
        pygame.display.update()
        client.subscribe("#")
        client.message_callback_add('engine/rpm/state', on_message_rpm)
        client.message_callback_add('engine/egt/state', on_message_egt)
        client.message_callback_add('engine/oilpressure/state', on_message_oilpressure)
        client.message_callback_add('engine/boost/state', on_message_boost)
        client.message_callback_add('engine/coolant/state', on_message_coolant)
        client.message_callback_add('engine/fuel/state', on_message_fuel)
        client.message_callback_add('cabin/outside_temp/state', on_message_outside_temp)
        client.message_callback_add('cabin/speed_cv/state', on_message_speed_cv)

        #on_message_rpm()
        #rpm_status = str(on_message_rpm)

    pygame.quit()


if __name__ == "__main__":
    main()
