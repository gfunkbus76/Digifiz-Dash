### NOTE: This is a work in progess, I'm not programmer or git expert, so I update straight to main branch... Sorry! ALSO the arduino code that is currently up is somewhat functional but definitely not finalized. That is the next focus.... (feb 2021) ###

# Digifiz-Dash v.03
### by GFunkbus76 / aka Gavin
## Check out http://www.youtube.com/GFunkbus76

 A pygame Dashboard mimicing the VW Digifiz Dash of the 80s. Powered by Raspberry pi4 and arduinos. This project was inspired by ManxGauged (on github) as well as supported by numerous online tutorials and google searches, I'm a cut, paste, edit and run coder... so beware. Sorry if I've used your experience and not thanked you! Tech with Tim, Coding by Mosh, Rik Cross and Christian Duenes on youtube all had good content I think! Thanks to DONE with ConsultDash(github) for some intial inspiration as well as Everlanders(youtube) oh yeah, also This Old Bus (has a canbus/node-red setup!).
 
 This has been a long term, evolving project started in 2019/2020. My project vehicle, a 1976 VW Bus has been customized and 
 includes a 1.9L AAZ Turbo Diesel engine upgrade. I wanted to also modernize some of the systems in the vehicle - mainly
 monitoring and entertainment. For entertainment, I'm currently using OpenAutoPro - it runs my 'head unit' part of the project.
 For the gauge cluster, I ended up going more one-off. As I'm going to be integrating various sensors, and not just plugging 
 in OBD2 or CANBUS - I have to decipher and interpret the data myself for display.
 
**This project has a few main areas:** 
  -Hardware 
      #-Raspberry Pi 4, 4gb as main computer
      #-Arduino Mega in engine bay transmitting via canbus currently (EGT, RPM, Boost, Oil Pressure, Coolant Temp, etc)
      #-Arduino Nano in front to receive and interpret canbus signals, connected to RPi via serial usb
      #-2nd Arduino Nano in cabin will probably function to do a variety of other sensors(ambient temp, gps, speedometer sensor)
      #-2x LCD Screens, 1x 7" Touch for the headunit, 1x 12.3" stretched LCD for the dashboard cluster
      #-Various sensors and modules (GPS, EGT, Pressure Transducers, optoisolators, buck converters etc)
  -Software
      -OpenAutoPro (use Coupon Code oap_2020 to save 5%) - I use this to manage the headunit and Android Auto portion
      -Digifiz Dash (main.py) - this is the main python/pygame code to run the dash
      -Mosquitto MQTT broker - set to run on Pi, it will publish the data from the Arduino to the Dash
      -Node-Red - used to manage MQTT processes
      
  -Mechanical
      -Wouldn't be much of a dash without a car to attach it to!
      -I've owned the bus since 2003 I think, still not done. So don't expect fast progression...
      -Have to finish the motor swap, hooking up of additional sensors then lots of testing.
      
**OKAY ... so, what's in this github?**
-main.py is the main program that runs and controls the pygame with python
-There is a folder for images and fonts, dive in and see. Image planning is important for using pygame.

#### NOT A PYTHON DEVELOPER!! ... THIS IS A HOBBY! ####
   If you've got tips or advice on how to clean up the code let me know!
   

 
 **Disclaimer:**
    -Not at all connected to or involved with VW. Using their logo for use in a VW with respect and admiration! Be gone lawyers!
    -This is not a tested or complete project, it represents  work-in-progress and should be treated as such.
    -Please check your local laws and guidelines if you wish to install this in a vehicle ....
 
# USE AT YOUR OWN RISK!
