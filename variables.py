

'''                        Dash Variables                        '''

#   Gauge State Variables --> fed from local MQTT Server
rpm_status = 0
coolant_status = 0
egt_status = 0
oilpressure_status = 0
boost_status = 0
fuel_status = 0
outside_temp_status = 0
speed_status = 0

#   MQTT Variables
broker_address = "localhost"  # Broker address
port = 1883  # Broker port


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
