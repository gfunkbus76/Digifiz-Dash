
######
#       MQTT Connection Function
######


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else: print("Connection failed")


def on_message(client, userdata, message): print(message.topic + " " + message.payload.decode())


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
    speed_cv_mqtt = int((message.payload.decode()))
    speed_status = speed_cv_mqtt


def on_message_speed_gps(digi, obj, message):
    global speed_gps_status
    speed_gps_mqtt = int((message.payload.decode()))
    speed_gps_status = speed_gps_mqtt


def on_message_outside_temp(digi, obj, message):
    global outside_temp_status
    outside_temp_mqtt = int((message.payload.decode()))
    outside_temp_status = outside_temp_mqtt


def on_message_fuel(digi, obj, message):
    global fuel_status
    fuel_mqtt = int((message.payload.decode()))
    fuel_status = fuel_mqtt


######
#       INDICATOR TOPIC MQTT
######

def on_message_illumination(digi, obj, message):
    global illumination_state
    illumination_mqtt = int((message.payload.decode()))
    illumination_state = illumination_mqtt


def on_message_foglight(digi, obj, message):
    global foglight_state
    foglight_mqtt = int((message.payload.decode()))
    foglight_state = foglight_mqtt


def on_message_defog(digi, obj, message):
    global defog_state
    defog_mqtt = int((message.payload.decode()))
    defog_state = defog_mqtt


def on_message_highbeam(digi, obj, message):
    global highbeam_state
    highbeam_mqtt = int((message.payload.decode()))
    highbeam_state = highbeam_mqtt


def on_message_leftturn(digi, obj, message):
    global leftturn_state
    leftturn_mqtt = int((message.payload.decode()))
    leftturn_state = leftturn_mqtt


def on_message_rightturn(digi, obj, message):
    global rightturn_state
    rightturn_mqtt = int((message.payload.decode()))
    rightturn_state = rightturn_mqtt


def on_message_brakewarn(digi, obj, message):
    global brakewarn_state
    brakewarn_mqtt = int((message.payload.decode()))
    brakewarn_state = brakewarn_mqtt


def on_message_oillight(digi, obj, message):
    global oillight_state
    oillight_mqtt = int((message.payload.decode()))
    oillight_state = oillight_mqtt


def on_message_alt(digi, obj, message):
    global alt_state
    alt_mqtt = int((message.payload.decode()))
    alt_state = alt_mqtt


def on_message_glow(digi, obj, message):
    global glow_state
    glow_mqtt = int((message.payload.decode()))
    glow_state = glow_mqtt
