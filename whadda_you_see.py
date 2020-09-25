"""

@@@@@@@@@@@@@@@@@@@@@@                                                                                                                               
@@@@@@@@@@@@@@@@@@@@@@             @@@.    @@@    @@@.     @@@@    @@@@        @@@@@@@@@        @@@@@@@@@@@@@.     .@@@@@@@@@@@@@        @@@@@@@@@  
@@@@@%%@@@%%@@@%%@@@@@             @@@@    @@@    @@@@     @@@@    @@@@       @@@@@@@@@@        @@@@@@@@@@@@@@     @@@@@@@@@@@@@@        @@@@@@@@@  
@@@@@  @@@  @@@  @@@@@             @@@@    @@@    @@@@     @@@@    @@@@       @@@@   @@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@   @@@@ 
@@@@@            @@@@@             @@@@   @@@@    @@@@     @@@@@@@@@@@@       @@@@   @@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@   @@@@ 
@@@@@   @    @   @@@@@             @@@@   @@@@    @@@@     @@@@@@@@@@@@       @@@@@@@@@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@@@@@@@@ 
@@@@@            @@@@@             @@@@###@@@@@##@@@@@     @@@@    @@@@      @@@@@@@@@@@@       #@@@@@###@@@@@     ##@@@@@###@@@@       @@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@     @@@@    @@@@      @@@@    @@@@@      @@@@@@@@@@@@@@     @@@@@@@@@@@@@@      @@@@     @@@@
@@@@@@@@@@@@@@@@@@@@@@

Project name: Whadda you see? (Raspberry pi edition)
Colour sensor Raspberry Pi Demo

Description:
  This project uses a colour sensor to determine the main colour of an object. 
  The Hue color parameter (a number that represents the "pure colour") is calculated based on the RGB-values that are read from the sensor. 
  From the Hue parameter it is possible to determine which basic color is presented to the sensor. 
  If the button (connected to GPIO pin 20) is pressed, the corresponding colour is printed on the terminal and can be heard using the on-board audio (using a Text-To-Speech program)

  More information on the working principles can be found on whadda.com

Level of difficulty: Intermediate

Parts required:
  - Raspberry Pi 3B/B+ or 4B or equivalent (e.g. Whadda PI4SET)
  - 0.96" or 1.3" OLED screen (e.g. Whadda INSERT WHADDA CODE/VMA437 1.3 INCH OLED SCREEN FOR ARDUINO or INSERT WHADDA CODE/VMA438 0.96 INCH OLED SCREEN WITH I2C FOR ARDUINO)
  - TCS3200 color sensor module (e.g. Whadda INSERT WHADDA CODE/VMA325 COLOR SENSOR TCS3200 MODULE)

See illustrated wiring diagram for the necessary connections, available on whadda.com

For more information, check out whadda.com

Required Python modules:
    - RPi.GPIO (should be installed by default, if not use folowing command to install: sudo apt install python-rpi.gpio python3-rpi.gpio)
    - Pillow (command to install: pip3 install Pillow)
    - adafruit_ssd1306 (command to install: pip3 install adafruit-circuitpython-ssd1306)

Code inspired by how to Mechatronics (https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/)

Author: Midas Gossye
(c) 2020 Whadda, premium makers brand by Velleman
"""

OLED_SCREEN_INSTALLED = True

# Import necessary modules
import RPi.GPIO as GPIO
from time import sleep
import time
import colorsys
import os
from PIL import Image, ImageDraw, ImageFont
import argparse

# Import the OLED modules if an OLED screen is installed
if OLED_SCREEN_INSTALLED:
    import adafruit_ssd1306
    from board import SCL, SDA
    import busio
########################################################

parser = argparse.ArgumentParser(prog='whadda_you_see', description='Determine and display colour from TCS3200 colour sensor')
parser.add_argument('--OLED', help='Add if OLED screen is installed', action='store_true', default='store_false')

parser.parse_args()
OLED_SCREEN_INSTALLED = OLED

GPIO.setmode(GPIO.BCM) # Use processor pin numbering system

NUM_CYCLES = 10 # number of measurements to perform to determine colour

# pin connections
S0 = 5      # S0 colour sensor
S1 = 6      # S1 colour sensor
S2 = 13     # 20 colour sensor
S3 = 19     # S3 colour sensor
Out = 26    # Out colour sensor
Button = 20 # Button
###############################

if OLED_SCREEN_INSTALLED:
    i2c = busio.I2C(SCL, SDA) # Initialize the I2C bus for the OLED screen

    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c) # Initialize OLED screen (128x64 pixels)
    oled.fill(0) # fill the screen with 0's (clear screen)

# setup GPIO pins (inputs/outputs)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(Out, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#####################################################

# pin reading sequence for Red, Green, Blue measurements [S2, S3]
pin_reading_seq = [[GPIO.LOW, GPIO.LOW], [GPIO.HIGH, GPIO.HIGH], [GPIO.LOW, GPIO.HIGH], [GPIO.HIGH, GPIO.LOW]]
##############################################################################################################


RGBW = [0, 0, 0, 0] # Initialize empty array to hold Red, Green, Blue & White colour sensor readings

# Set colour frequency scaling to 2% / 12 kHz
GPIO.output(S0, GPIO.LOW)
GPIO.output(S1, GPIO.HIGH)

colour_names = ['Red', 'Green', 'Blue', 'White']



if OLED_SCREEN_INSTALLED:
    # Show Raspberry Pi Logo on OLED screen for 1 sec
    image = Image.open("RPI.bmp") 
    oled.image(image)
    oled.show()
    sleep(1)
    ##################################################

    oled.fill(0) # fill the screen with 0's (clear screen)

    # Show Whadda Logo on OLED screen for 2 secs
    image = Image.open("WHADDA.bmp")
    oled.image(image)
    oled.show()
    sleep(2)
    ##################################################


    # Open a new blank image and draw object to later draw tex and shapes on
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    #########################################################################

    oled.fill(0) # fill the screen with 0's (clear screen)

    # Load a font in 2 different sizes.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

    # Draw the text that doesn't need updating
    draw.text((0, 0), "Red: ", font=font, fill=255, align="right")
    draw.text((0, 10), "Green: ", font=font, fill=255, align="right")
    draw.text((0, 20), "Blue: ", font=font, fill=255, align="right")


    draw.text((70, 0), "Hue: ", font=font, fill=255, align="right")
    draw.text((70, 10), "Sat.: ", font=font, fill=255, align="right")
    draw.text((70, 20), "Value: ", font=font, fill=255, align="right")
    ##################################################################

    draw.line((64, 0, 64, 32), width=1, fill=255)  # draw vertical seperation line
    draw.line((0, 32, 127, 32), width=1, fill=255) # draw horizontal seperation line

    # Update image on OLED
    oled.image(image)
    oled.show()
    ######################

"""
Function descrition:
    Reads the Red, Green, Blue & White colour components from the TCS3200 colour sensor,
    converts the RGB colour into the HSV colour space, determines the colour name from the Hue value,
    and displays all of the above information on the OLED screen.

Arguments:
    None

Returns:
    -color_str (String with the colour name)
    -HSV_Val (list with Hue, Saturation and Value components respectively)
"""
def read_color():
    for idx, pin_states in enumerate(pin_reading_seq):
        # Select colour filter
        GPIO.output(S2, pin_states[0])
        GPIO.output(S3, pin_states[1])
        ##############################
        time.sleep(0.01)

        start = time.time() # start timing measurement to time pulse length

        # Wait until the NUM_cycles pulses have been counted
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(Out, GPIO.FALLING)
        ####################################################

        duration = time.time() - start # calculate duration of pulses
        RGBW[idx] = ((NUM_CYCLES / duration) / 10000) *255 # compute Red, Green and White colour components and scale to 0-255

    # Scale Red, Green & Blue components with respect to the White/Brightness reading
    RGBW[0] = (RGBW[0] /RGBW[3]) 
    RGBW[1] = (RGBW[1] / RGBW[3])
    RGBW[2] = (RGBW[2] / RGBW[3])
    #################################################################################

    HSV_val = colorsys.rgb_to_hsv(RGBW[0], RGBW[1], RGBW[2]) # Convert RGB colour readings into HSV colour space
    
    color_str = ""
    
    # Convert Red, Green & Blue values to rounded percentages
    R_perc = round(RGBW[0]*100)
    G_perc = round(RGBW[1]*100)
    B_perc = round(RGBW[2]*100)
    #########################################################

    hue_deg = round(HSV_val[0]*360) # Convert Hue to rounded degrees

    # Convert value and saturation to rounded percentages
    val_perc = round(HSV_val[1]*100)
    sat_perc = round(HSV_val[2]*100)
    #####################################################

    
    if OLED_SCREEN_INSTALLED:
        # draw "black" rectangle to clear screen space for updated numbers
        draw.rectangle((34, 0, 63, 30), fill=0)
        draw.rectangle((100, 0, 127, 30), fill=0)
        ###################################################################

        # Put updated Red, Green and Blue percentages on screen
        draw.text((30, 0), "{:3d} %".format(R_perc), font=font, fill=255, align="right")
        draw.text((30, 10), "{:3d} %".format(G_perc), font=font, fill=255, align="right")
        draw.text((30, 20), "{:3d} %".format(B_perc), font=font, fill=255, align="right")
        #################################################################################

        # Put updated Hue, value and saturation numbers on screen
        draw.text((100, 0), "{:3d} °".format(hue_deg), font=font, fill=255, align="right")
        draw.text((100, 10), "{:3d} %".format(val_perc), font=font, fill=255, align="right")
        draw.text((100, 20), "{:3d} %".format(sat_perc), font=font, fill=255, align="right")
        ####################################################################################
    
    # Determine colour based on hue parameter
    if sat_perc < 35:
        color_str = "Black/Dark"
    elif hue_deg > 357 or hue_deg < 10:
        color_str = "ORANGE"
    elif hue_deg > 10 and hue_deg < 40:
        color_str = "YELLOW"
    elif hue_deg > 45 and hue_deg < 160:
        color_str = "GREEN"
    elif hue_deg > 210 and hue_deg < 270:
        color_str = "BLUE"
    elif hue_deg > 270 and hue_deg < 330:
        color_str ="PURPLE"
    elif hue_deg > 340 and hue_deg < 356:
        color_str = "RED"
    else:
        color_str = "No valid color detected"
    #########################################

    if OLED_SCREEN_INSTALLED:
        draw.rectangle((0, 34, 128, 60), fill=0) # clear bottom part of screen by drawing "black" rectangle

        # if a valid color is detected...
        if color_str != "No valid color detected" and color_str != "Black/Dark":
            draw.rectangle((0, 34, 128, 60), fill=255)                  # Draw a filled rectangle as background
            w, h = draw.textsize(color_str, font=font2)                 # Calculate pixel width and height of color name
            draw.text(((128-w)/2, 33), color_str, font=font2, fill=0)   # Put color name on screen with inversed text
            
        # Update OLED screen with new image
        oled.image(image) 
        oled.show()
        ###################################

    return color_str, HSV_val

while True:
    color_str, HSV_val = read_color() # Read and display colour name and values

    # If button is pressed...
    if GPIO.input(Button) == GPIO.LOW:        
        # Print colour details on terminal
        print("Detected color: {}".format(color_str))
        print("Hue:", HSV_val[0]*360)
        print("\n")
        ##################################
 
        # Using the Pico Text-To-Speech program SAY the colour
        os.system('pico2wave -w tts.wav "{}" && aplay tts.wav'.format(color_str))

        print("=================")
        print("\n")
        