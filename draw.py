'''
A place for my main draw functions.
Just an attempt to clean up the main file.
'''
from main import *



def mileage():
    '''
    Text File or Odometer and Tripometer Information (pulled from ManxGauged project, just reads from text file
    Need to incorporate writing to the file after I figure out how to tabulate the mileage based on GPS or CV
    '''
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

    #   Drawing the Odometer
    digital_odo = odometer
    odo_text = odo_font.render(str(digital_odo), True, NEON_GREEN)
    text_rect = odo_text.get_rect()
    text_rect.midright = ODO_L_XY
    WIN.blit(odo_text, text_rect)


def draw_clock():
    '''
    Drawing the clock - currently only 24hr. I'm sure its easy to adapt to 12hr.
    '''
    now = datetime.now()
    bgclock_text = digital_font.render("00:00", True, DARK_GREY)
    WIN.blit(bgclock_text, CLOCK_XY)
    digital_text = now.strftime('%H:%M')
    text = digital_font.render(digital_text, True, NEON_GREEN)
    WIN.blit(text, CLOCK_XY)

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

def draw_mfa():
    '''
    Drawing the clock and interior temp - should seperate as the MFA will eventually evolve.
    '''
    global outside_temp_status

    WIN.blit(MFA, MFABG_XY)
    #   Draw MFA display
    text = digital_font.render(str(outside_temp_status), True, NEON_GREEN)
    #   Enables the text to be right center aligned
    text_rect = text.get_rect()
    text_rect.midright = MFA_XY
    WIN.blit(text, text_rect)




def draw_indicators():
    '''
    The area where I blit or draw the indicators/idiot lights and turn signals/low fuel etc.

    '''

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

    #   To highlight the fuel reserve indicator (factory is at 7 litres
    if fuel_status <= 7:
        WIN.blit(fuelresOn, (1795, 616))
    else:
        WIN.blit(fuelresOff, (1795, 616))