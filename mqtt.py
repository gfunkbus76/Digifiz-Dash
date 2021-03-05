import paho.mqtt.client as mqttClient
from constants import *

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
    global rpm_status
    global rpm_mqtt
    rpm_mqtt = int((message.payload.decode())[0:6])
    rpm_status = rpm_mqtt


def on_message_coolant(digi, obj, message):
    global coolant_status
    global coolant_mqtt
    coolant_mqtt = int((message.payload.decode())[0:6])
    coolant_status = coolant_mqtt


def on_message_egt(digi, obj, message):
    global egt
    global egt_status
    global egt_mqtt
    global egt_update
    egt.set_frame = 0
    egt_mqtt = int((message.payload.decode())[0:6])
    #egt_status = egt_mqtt
    #egt_update += int(egt_mqtt)
    #egt_status = egt_update
    egt.set_frame(egt_mqtt)
    #egt_status = gauge1.status
'''    print(egt_mqtt)
    print("MQTT update: "+ str(egt_update))
    print("MQTT  status: "+ str(egt_status))'''

def on_message_oilpressure(digi, obj, message):
    global oilpressure_status
    global oilpressure_mqtt
    oilpressure_mqtt = int((message.payload.decode())[0:6])
    oilpressure_status = oilpressure_mqtt


def on_message_boost(digi, obj, message):
    global boost_status
    global boost_mqtt
    boost_mqtt = int((message.payload.decode())[0:6])
    boost_status = boost_mqtt


######
#       CABIN TOPIC MQTT
######

def on_message_speed_cv(digi, obj, message):
    global speed_status
    global speed_cv_mqtt
    speed_cv_mqtt = int((message.payload.decode())[0:6])
    speed_status = speed_cv_mqtt


def on_message_speed_gps(digi, obj, message):
    global speed_gps_status
    global speed_gps_mqtt
    speed_gps_mqtt = int((message.payload.decode())[0:6])
    speed_gps_status = speed_gps_mqtt


def on_message_outside_temp(digi, obj, message):
    global outside_temp_status
    global outside_temp_mqtt
    outside_temp_mqtt = int((message.payload.decode())[0:6])
    outside_temp_status = outside_temp_mqtt


def on_message_fuel(digi, obj, message):
    global fuel_status
    global fuel_mqtt
    fuel_mqtt = int((message.payload.decode())[0:6])
    fuel_status = fuel_mqtt


######
#       INDICATOR TOPIC MQTT
######

def on_message_illumination(digi, obj, message):
    global illumination_state
    global illumination_mqtt
    illumination_mqtt = int((message.payload.decode())[0:6])
    illumination_state = illumination_mqtt


def on_message_foglight(digi, obj, message):
    global foglight_state
    global foglight_mqtt
    foglight_mqtt = int((message.payload.decode())[0:6])
    foglight_state = foglight_mqtt


def on_message_defog(digi, obj, message):
    global defog_state
    global defog_mqtt
    defog_mqtt = int((message.payload.decode())[0:6])
    defog_state = defog_mqtt


def on_message_highbeam(digi, obj, message):
    global highbeam_state
    global highbeam_mqtt
    highbeam_mqtt = int((message.payload.decode())[0:6])
    highbeam_state = highbeam_mqtt


def on_message_leftturn(digi, obj, message):
    global leftturn_state
    global leftturn_mqtt
    leftturn_mqtt = int((message.payload.decode())[0:6])
    leftturn_state = leftturn_mqtt


def on_message_rightturn(digi, obj, message):
    global rightturn_state
    global rightturn_mqtt
    rightturn_mqtt = int((message.payload.decode())[0:6])
    rightturn_state = rightturn_mqtt


def on_message_brakewarn(digi, obj, message):
    global brakewarn_state
    global brakewarn_mqtt
    brakewarn_mqtt = int((message.payload.decode())[0:6])
    brakewarn_state = brakewarn_mqtt


def on_message_oillight(digi, obj, message):
    global oillight_state
    global oillight_mqtt
    oillight_mqtt = int((message.payload.decode())[0:6])
    oillight_state = oillight_mqtt


def on_message_alt(digi, obj, message):
    global alt_state
    global alt_mqtt
    alt_mqtt = int((message.payload.decode())[0:6])
    alt_state = alt_mqtt


def on_message_glow(digi, obj, message):
    global glow_state
    global glow_mqtt
    glow_mqtt = int((message.payload.decode())[0:6])
    glow_state = glow_mqtt
