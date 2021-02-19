#!/usr/bin/python3
 
###################################################################
#                                                                 #
# Small script to read data from Arduino serial port and publish  #
# the data to the specified MQTT topic.                           #
#                                                                 #
###################################################################
 
 
# Need to import some stuff to make magic happen :)
 
import serial
import time
import paho.mqtt.client as mqtt
import sys
import datetime
ser = serial.Serial('/dev/ttyACM0', 9600 ) # This is the emulated or physical USB port
time.sleep(2)
 
# Variables what you need to change
 
datetime = datetime.datetime.now() # This was left from a former script
username = "your_username"
password = "your_super_secret_password"
clientid = "Arduino"
 
# Let's connect to my MQTT server 
 
mqttc = mqtt.Client(client_id=clientid)
mqttc.username_pw_set(username, password=password)
mqttc.connect("127.0.0.1", port=1883, keepalive=60)
mqttc.loop_start()
 
topic_dioda = "v1/" + username + "/things/" + clientid + "/dioda"
topic_DHTTemp = "v1/" + username + "/things/" + clientid + "/DHTTemp"
topic_DHTHum = "v1/" + username + "/things/" + clientid + "/DHTHum"
topic_feny = "v1/" + username + "/things/" + clientid + "/feny"
 
 
 
while True:
    try:
        b = ser.readline()
        string_n = b.decode()
        string = string_n.rstrip()
        
 
        if string.startswith("Hum"):
            print(f"Ez itt a paratartalom {string}")
            s = (string[7:12]) # want to grab only the numerical value from the string
            print(s) 
            s = str(s)            
            mqttc.publish(topic_DHTHum, payload=s, retain=True) # publish it to the proper topic
        elif string.startswith("DHT", 4 ):
            print(f"Ez itt a DHT homerseklet {string}")
            s1 = (string[8:13])
            print(s1)
            mqttc.publish(topic_DHTTemp, payload=s1,retain=True)
        elif string.startswith("Temp"):
 
            print(f"Whoop whoop dioda {string}")
            s3 = (string[5:10])
            print(s3)
            mqttc.publish(topic_dioda, payload=s3,retain=True)
        elif string.startswith("Feny"):
            print(f"Ez itt a feny {string}")
            s4 = (string[6:11])
            mqttc.publish(topic_feny, payload=s4,retain=True)
           
        time.sleep(0.1)
    except (EOFError, SystemExit, KeyboardInterrupt):
    
        print("Interrupt!!")
        break
        ser.close()
        mqttc.disconnect()
        sys.exit()
 
 
