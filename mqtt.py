import paho.mqtt.client as mqttClient

class PahoImport(object):

    def __init__(self):
        try:
            self.broker_address = "localhost"
            self.port = 1883
            self.client = mqttClient.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.broker_address, port=self.port)

            logging.info("Connected to {0}, starting MQTT loop".format(self.broker_address))
            self.client.loop_start()
        except Exception as e:
            print(e)

    def on_connect(self, client, userdata, flags, rc):
        print("connected!")
        self.client.subscribe("TRACED")


    ######
    #       MQTT Connection Function
    ######

    def on_connect(self, client, userdata, flags, rc):
        if self.rc == 0:
            print("Connected to broker")
            global Connected  # Use global variable
            Connected = True  # Signal connection
        else:
            print("Connection failed")


    def on_message(self, client, userdata, message):
        print(self.message.topic + " " + self.message.payload.decode())


    ######
    #       ENGINE TOPIC MQTT
    ######

    def on_message_rpm(self, obj, message):
        rpm_mqtt = int((self.message.payload.decode()))
        rpm.set_frame(rpm_mqtt)


    def on_message_coolant(self, obj, message):
        coolant_mqtt = int((self.message.payload.decode()))
        coolant.set_frame(coolant_mqtt)


    def on_message_egt(self, obj, message):
        egt_mqtt = int((self.message.payload.decode()))
        egt.set_frame(egt_mqtt)


    def on_message_oilpressure(self, obj, message):
        oilpressure_mqtt = int((self.message.payload.decode()))
        oilpressure.set_frame(oilpressure_mqtt)


    def on_message_boost(self, obj, message):
        boost_mqtt = int((self.message.payload.decode()))
        boost.set_frame(boost_mqtt)


    ######
    #       CABIN TOPIC MQTT
    ######

    def on_message_speed_cv(self, obj, message):
        global speed_status
        global speed_cv_mqtt
        speed_cv_mqtt = int((self.message.payload.decode()))
        speed_status = speed_cv_mqtt


    def on_message_speed_gps(self, obj, message):
        global speed_gps_status
        global speed_gps_mqtt
        speed_gps_mqtt = int((self.message.payload.decode()))
        speed_gps_status = speed_gps_mqtt


    def on_message_outside_temp(self, obj, message):
        global outside_temp_status
        global outside_temp_mqtt
        outside_temp_mqtt = int((self.message.payload.decode()))
        outside_temp_status = outside_temp_mqtt


    def on_message_fuel(self, obj, message):
        global fuel_status
        global fuel_mqtt
        fuel_mqtt = int((self.message.payload.decode()))
        fuel_status = fuel_mqtt


    ######
    #       INDICATOR TOPIC MQTT
    ######

    def on_message_illumination(self, obj, message):
        global illumination_state
        global illumination_mqtt
        illumination_mqtt = int((self.message.payload.decode()))
        illumination_state = illumination_mqtt


    def on_message_foglight(self, obj, message):
        global foglight_state
        global foglight_mqtt
        foglight_mqtt = int((self.message.payload.decode()))
        foglight_state = foglight_mqtt


    def on_message_defog(self, obj, message):
        global defog_state
        global defog_mqtt
        defog_mqtt = int((self.message.payload.decode()))
        defog_state = defog_mqtt


    def on_message_highbeam(self, obj, message):
        global highbeam_state
        global highbeam_mqtt
        highbeam_mqtt = int((self.message.payload.decode()))
        highbeam_state = highbeam_mqtt


    def on_message_leftturn(self, obj, message):
        global leftturn_state
        global leftturn_mqtt
        leftturn_mqtt = int((self.message.payload.decode()))
        leftturn_state = leftturn_mqtt


    def on_message_rightturn(self, obj, message):
        global rightturn_state
        global rightturn_mqtt
        rightturn_mqtt = int((self.message.payload.decode()))
        rightturn_state = rightturn_mqtt


    def on_message_brakewarn(self, obj, message):
        global brakewarn_state
        global brakewarn_mqtt
        brakewarn_mqtt = int((self.message.payload.decode()))
        brakewarn_state = brakewarn_mqtt


    def on_message_oillight(self, obj, message):
        global oillight_state
        global oillight_mqtt
        oillight_mqtt = int((self.message.payload.decode()))
        oillight_state = oillight_mqtt


    def on_message_alt(self, obj, message):
        global alt_state
        global alt_mqtt
        alt_mqtt = int((self.message.payload.decode()))
        alt_state = alt_mqtt


    def on_message_glow(self, obj, message):
        global glow_state
        global glow_mqtt
        glow_mqtt = int((self.message.payload.decode()))
        glow_state = glow_mqtt

    def callbacks(self):
        #   MQTT Call backs... putting values in from topics

        self.client.subscribe("#") #     Subscribes to all topics
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


