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

Code inspired by how to Mechatronics (https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/)

Author: Midas Gossye
(c) 2020 Whadda, premium makers brand by Velleman
"""

# Import necessary modules
import RPi.GPIO as GPIO
from time import sleep
import time
import colorsys
import os
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont

# Import the SSD1306 module.
import adafruit_ssd1306

GPIO.setmode(GPIO.BCM) # Use processor pin numbering system

NUM_CYCLES = 10 # number of measurements to perform to determine colour

# pin connections
S0 = 5
S1 = 6
S2 = 13
S3 = 19
Out = 26
Button = 20
##################

i2c = busio.I2C(SCL, SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
image = Image.open("RPI.bmp")
oled.image(image)
oled.show()
sleep(1)
oled.fill(0)
image = Image.open("WHADDA.bmp")
oled.image(image)
oled.show()
sleep(2)



image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
oled.fill(0)
# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

# Draw the text
draw.text((0, 0), "Red: ", font=font, fill=255, align="right")
draw.text((0, 10), "Green: ", font=font, fill=255, align="right")
draw.text((0, 20), "Blue: ", font=font, fill=255, align="right")

draw.text((70, 0), "Hue: ", font=font, fill=255, align="right")
draw.text((70, 10), "Sat.: ", font=font, fill=255, align="right")
draw.text((70, 20), "Value: ", font=font, fill=255, align="right")

draw.line((64, 0, 64, 32), width=1, fill=255)
draw.line((0, 32, 127, 32), width=1, fill=255)

# Display image
oled.image(image)
oled.show()
# set pin 
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(Out, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pin_reading_seq = [[GPIO.LOW, GPIO.LOW], [GPIO.HIGH, GPIO.HIGH], [GPIO.LOW, GPIO.HIGH], [GPIO.HIGH, GPIO.LOW]]
RGBW = [0, 0, 0, 0]

GPIO.output(S0, GPIO.LOW)
GPIO.output(S1, GPIO.HIGH)

colour_names = ['Red', 'Green', 'Blue', 'White']


def read_color():
    for idx, pin_states in enumerate(pin_reading_seq):
        GPIO.output(S2, pin_states[0])
        GPIO.output(S3, pin_states[1])
        time.sleep(0.01)

        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(Out, GPIO.FALLING)
        duration = time.time() - start
        RGBW[idx] = ((NUM_CYCLES / duration) / 10000) *255

    RGBW[0] = (RGBW[0] /RGBW[3])
    RGBW[1] = (RGBW[1] / RGBW[3])
    RGBW[2] = (RGBW[2] / RGBW[3])

    HSV_val = colorsys.rgb_to_hsv(RGBW[0], RGBW[1], RGBW[2])
    color_str = ""
    
    R_perc = round(RGBW[0]*100)
    G_perc = round(RGBW[1]*100)
    B_perc = round(RGBW[2]*100)
    hue_deg = round(HSV_val[0]*360)
    val_perc = round(HSV_val[1]*100)
    sat_perc = round(HSV_val[2]*100)

    draw.rectangle((30, 0, 63, 30), fill=0)
    draw.rectangle((100, 0, 127, 30), fill=0)
    draw.text((30, 0), "{:3d} %".format(R_perc), font=font, fill=255, align="right")
    draw.text((30, 10), "{:3d} %".format(G_perc), font=font, fill=255, align="right")
    draw.text((30, 20), "{:3d} %".format(B_perc), font=font, fill=255, align="right")

    draw.text((100, 0), "{:3d} °".format(hue_deg), font=font, fill=255, align="right")
    draw.text((100, 10), "{:3d} %".format(val_perc), font=font, fill=255, align="right")
    draw.text((100, 20), "{:3d} %".format(sat_perc), font=font, fill=255, align="right")
    
    if HSV_val[2] < 0.35:
        color_str = "Black/Dark"
    elif HSV_val[0] > (357/360) or HSV_val[0] < (10/360):
        color_str = "ORANGE"
    elif HSV_val[0] > (10/360) and HSV_val[0] < (40/360):
        color_str = "YELLOW"
    elif HSV_val[0] > (45/360) and HSV_val[0] < (160/360):
        color_str = "GREEN"
    elif HSV_val[0] > (210/360) and HSV_val[0] < (270/360):
        color_str = "BLUE"
    elif HSV_val[0] > (270/360) and HSV_val[0] < (330/360):
        color_str ="PURPLE"
    elif HSV_val[0] > (340/360) and HSV_val[0] < (356/360):
        color_str = "RED"
    else:
        color_str = "No valid color detected"

    draw.rectangle((0, 34, 128, 60), fill=0)
    if color_str != "No valid color detected" and color_str != "Black/Dark":
        draw.rectangle((0, 34, 128, 60), fill=255)

        w, h = draw.textsize(color_str, font=font2)


        draw.text(((128-w)/2, 33), color_str, font=font2, fill=0)
        
    oled.image(image)
    oled.show()

    return color_str, HSV_val

while True:
    color_str, HSV_val = read_color()
    if GPIO.input(Button) == GPIO.LOW:        
        print("Detected color: {}".format(color_str))
        print("Hue:", HSV_val[0]*360)
        print("\n")
 
        os.system('pico2wave -w tts.wav "{}" && aplay tts.wav'.format(color_str))
        print("=================")
        print("\n")
        