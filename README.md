# Whadda you see?

![](./pictures/demo.jpg)

Are you always having discussions with other people (or even yourselves) what colour a certain object has? If you build this project that will all be in the past! Using your raspberry pi and a colour sensor we can make a cool gadget that determines the precise main colour of an object. It can even SAY what the colour is using a Text-To-Speech module. 

## Project description - How Does it work?

### What can this project do?
This project uses a colour sensor to determine the main colour of an object.
 The Hue color parameter (a number that represents the "pure colour tint") is calculated based on the RGB-values that are read from the sensor.
From the Hue parameter it is possible to determine which basic color is presented to the sensor. 
If the button (connected to GPIO pin 20) is pressed, the corresponding colour is printed on the terminal and can be heard using the on-board audio (using a Text-To-Speech program). Optionally, you can also attach an OLED screen and all of the regular RGB and HSV colour parameters will be displayed, together with the determined colour.

### You will need to do the following things for the project to work:

### Level of difficulty: Intermediate

## MATERIALS

### Ingredients:
*  Raspberry Pi 3B/B+ or 4B set (e.g. [Whadda PI4SET](https://www.vellemanformakers.com/product/raspberry-pi-4-2gb-starter-kit-pi4set/))
    - Raspberry Pi (3B/B+ or 4B)
    - Good quality USB power supply
    - \>= 8 GB MicroSD Card
* Basic electronics parts (e.g. Whadda [RPi DIY Kit (VMP501)](https://www.vellemanformakers.com/product/diy-kit-for-raspberry-pi-vmp501/) or [RPi electronics parts pack (VMP500)](https://www.vellemanformakers.com/product/electronic-parts-pack-for-raspberry-pi-vmp500/))
  - Breadboard
  - Pushbutton
  - Jumper cables (Female to Female & Male to Female)
  - [OPTIONAL] RPi GPIO Extension board
* TCS3200 color sensor module (e.g. [Whadda INSERT WHADDA CODE/VMA325 COLOR SENSOR TCS3200 MODULE](https://www.vellemanformakers.com/product/color-sensor-tcs3200-module-vma325/))
* [OPTIONAL] 0.96" OLED screen (e.g. [Whadda INSERT WHADDA CODE/VMA438 0.96" OLED SCREEN WITH I2C FOR ARDUINO](https://www.vellemanformakers.com/product/0-96-inch-oled-screen-with-i2c-for-arduino-vma438/))

### Tools:
* Working locally on Raspberry Pi:
  - HDMI Screen/monitor
  - USB Keyboard
  - USB Mouse
  - Internet connection (WiFi or wired ethernet)
* Working remotely on pc:
    - PC
    - RPi & PC connected to same network (WiFI or wired ethernet)

## PROGRAMMING  the development board

### Dev board: Raspberry Pi (3B/B+, 4B)

### Code language: Python (3)

### Difficulty: Intermediate

### Preperations:

1) If you don't have a (recent) version of Raspberry Pi OS installed on the Pi's microSD card, go to [raspberrypi.org/downloads](https://www.raspberrypi.org/downloads/) and download the latest version of raspberry Pi OS. Use the Raspberry Pi Imager (also available for download on [raspberrypi.org/downloads](https://www.raspberrypi.org/downloads/)) to flash the MicroSD card with the downloaded OS image. 

From this point on there are 2 ways to configure the pi: **on the pi itself** by connecting the necessary peripherals (mouse, keyboard and screen) to it directly, or **using your pc to connect to it remotely**. If you plan to use the 1st option you can skip step 2 and proceed directly to step 3.

2) If you want to use WiFi follow [this guide](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) to configure the WiFi access details before you proceed. 
Navigate to the SD Card partition named ```BOOT``` and add an empty file called ```ssh```. Make sure that this file doesn't have a file extension. In Windows you might need to check the ```File name extensions``` box in the View tab in file explorer to be able to do this.

3) Insert the MicroSD card into the Pi and connect all of your peripherals (if you're planning to use a seperate monitor). Also plugin a network cable if you're planning to use a wired ethernet connection. Power up the pi by connecting it to the USB power supply adapter.

4) Wait 2-3 min until the pi is fully booted. If you're using a seperate monitor, run through the initial Raspberry Pi OS setup wizard to configure network connections, etc... 
If you're connecting to the pi remotely, go to your network router setup webpage or use an IP-scanner (e.g. [Angry IP Scanner](https://angryip.org/download/)) to find the assigned IP-address of your pi and connect to it by opening Powershell/Terminal and type in the following command: ```ssh pi@<REPLACE WITH IP ADDRESS>```. The default password is ```raspberry```.

5) To make sure your pi is fully up-to-date, run the following command: ```sudo apt update && sudo apt upgrade -y```

6) Enable the I2C interface (necessary to use the OLED display) by running ```sudo raspi-config``` and selecting ```5 Interfacing Options > P5 I2C > Yes```.

## Installing necessary software

Run the following commands:

1) Make sure the python package manager (pip) is installed:
```
sudo apt-get install python3-pip
```

2) Install git client so we can easily download the project code
```
sudo apt-get install git
```

3) Download the project code
```
git clone https://github.com/Whaddadraft/Whadda_you_see_RPi.git && cd ./Whadda_you_see
```

4) Install the Text-To-Speech module using our install script:
```
sudo chmod +x install_tts.sh && sudo ./install_tts.sh
```

5) Install the required python modules:
```
pip3 install -r requirements.txt
```

## Prepping the connection

![](./pictures/fritzing_RPi_bb.png)

## Run the program!

```
python3 whadda_you_see.py
```