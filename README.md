# Raspberry Pi color checking project

![](https://cdn.whadda.com/wp-content/uploads/2021/03/04135205/2-3-800x600.jpg)

A Raspberry Pi is useful in all kinds of ways, even if you are looking to make a project that can help people increase the quality of their lives. This project is meant for people who are colourblind or have trouble seeing. Using your raspberry pi and a colour sensor, we can make a cool gadget that determines the precise main colour of an object. It can even say what colour it is detecting by using a Text-To-Speech module.

## Project description - How Does it work?

### How does it work?
This project uses a colour sensor to determine the main colour of an object. The Hue colour parameter (a number that represents the “pure colour tint”) is calculated based on the RGB-values that are read from the sensor. From the Hue parameter, it is possible to determine which basic colour is presented to the sensor. If the button (connected to GPIO pin 20) is pressed, the corresponding colour is printed on the terminal and can be heard using the on-board audio (using a Text-To-Speech program). Optionally, you can also attach an OLED screen and all of the regular RGB and HSV colour parameters will be displayed, together with the determined colour.

### You will need to do the following things for the project to work:

### Level of difficulty: intermediate

## MATERIALS

### Ingredients:
*  Raspberry Pi 3B/B+ or 4B set (e.g. [Whadda PI4SET](https://whadda.com/product/raspberry-pi-4-2gb-starter-kit-pi4set/))
    - Raspberry Pi (3B/B+ or 4B)
    - Good quality USB power supply
    - \>= 8 GB MicroSD Card
* Basic electronics parts (e.g. Whadda [RPi DIY Kit (WPK801/VMP501)](https://whadda.com/product/diy-kit-for-raspberry-pi-vmp501/) or [RPi electronics parts pack (WPK800/VMP500)](https://whadda.com/product/electronic-parts-pack-for-raspberry-pi-vmp500/))
  - Breadboard
  - Pushbutton
  - Jumper cables (Female to Female & Male to Female)
  - [OPTIONAL] RPi GPIO Extension board
* TCS3200 color sensor module (e.g. [Whadda WPSE325/VMA325 COLOR SENSOR TCS3200 MODULE](https://whadda.com/product/color-sensor-tcs3200-module-vma325/))
* [OPTIONAL] 0.96" OLED screen (e.g. [Whadda WPI438/VMA438 0.96" OLED SCREEN WITH I2C FOR ARDUINO](https://whadda.com/product/0-96-inch-oled-screen-with-i2c-for-arduino-vma438/))

<table class="table table-hover table-striped table-bordered">
  <tr align="center">
   <td><a href="https://whadda.com/product/raspberry-pi-4-2gb-starter-kit-pi4set/"><img src="https://cdn.whadda.com/wp-content/uploads/2020/01/27104737/pi4set-2.jpg" alt="Whadda Pi 4 starter kit"></a></td>
   <td><a href="https://whadda.com/product/color-sensor-tcs3200-module-vma325/"><img src="https://cdn.whadda.com/wp-content/uploads/2019/02/27100921/vma325.jpg" alt="Whadda TCS3200 colour sensor"></a></td>
  </tr>
  <tr align="center">
    <td><i><a href="https://whadda.com/product/raspberry-pi-4-2gb-starter-kit-pi4set">Whadda Raspberry Pi 4 starter set</a></i></td>
    <td><i><a href="https://whadda.com/product/color-sensor-tcs3200-module-vma325/">Whadda TCS3200 colour sensor</a></i></td>
  </tr>
    <tr align="center">
   <td><a href="https://whadda.com/product/diy-kit-for-raspberry-pi-vmp501/"><img src="https://cdn.whadda.com/wp-content/uploads/2019/02/27100807/vmp501.jpg" alt="Whadda RPi DIY kit"></a></td>
   <td><a href="https://whadda.com/product/0-96-inch-oled-screen-with-i2c-for-arduino-vma438/"><img src="https://cdn.whadda.com/wp-content/uploads/2019/02/27100949/vma438.jpg" alt="Whadda 0.96'' OLED screen"></a></td>
  </tr>
  <tr align="center">
    <td><i><a href="https://whadda.com/product/diy-kit-for-raspberry-pi-vmp501/">Whadda Raspberry Pi DIY kit</a></i></td>
    <td><i><a href="https://whadda.com/product/0-96-inch-oled-screen-with-i2c-for-arduino-vma438/">Whadda 0.96" OLED screen</a></i></td>
  </tr>
</table>

### Tools:
* Working locally on Raspberry Pi:
  - HDMI Screen/monitor
  - USB Keyboard
  - USB Mouse
  - Internet connection (WiFi or wired ethernet)
* Working remotely on pc:
    - PC
    - RPi & PC connected to same network (WiFi or wired ethernet)

## PROGRAMMING  the development board

### Dev board: Raspberry Pi (3B/B+, 4B)

### Code language: Python (3)

### Difficulty: Intermediate

### Preparations:

1) If you don't have a (recent) version of Raspberry Pi OS installed on the Pi's microSD card, go to [raspberrypi.org/downloads](https://www.raspberrypi.org/downloads/) and download the latest version of the Raspberry Pi Imager. Use the Raspberry Pi Imager to flash the MicroSD card with the latest verion of Raspberry Pi OS. 

From this point on there are 2 ways to configure the pi: **on the pi itself** by connecting the necessary peripherals (mouse, keyboard and screen) to it directly, or **using your pc to connect to it remotely**. If you plan to use the 1st option you can skip step 2 and proceed directly to step 3.

2) If you want to use WiFi follow [this guide](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) to configure the WiFi access details before you proceed. 
Navigate to the SD Card partition named ```BOOT``` and add an empty file called ```ssh```. Make sure that this file doesn't have a file extension. In Windows you might need to check the ```File name extensions``` box in the View tab in file explorer to be able to do this.

3) Insert the MicroSD card into the Pi and connect all of your peripherals (if you're planning to use a seperate monitor). Also plugin a network cable if you're planning to use a wired ethernet connection. Power up the pi by connecting it to the USB power supply adapter.

4) Wait 2-3 min until the pi is fully booted. If you're using a seperate monitor, run through the initial Raspberry Pi OS setup wizard to configure network connections, etc... 
If you're connecting to the pi remotely, go to your network router setup webpage or use an IP-scanner (e.g. [Angry IP Scanner](https://angryip.org/download/)) to find the assigned IP-address of your pi and connect to it by opening Powershell/Terminal and type in the following command: ```ssh pi@<REPLACE WITH IP ADDRESS>```. The default password is ```raspberry```.

5) To make sure your pi is fully up-to-date, run the following command: ```sudo apt update && sudo apt upgrade -y```

6) Enable the I2C interface (necessary to use the OLED display) by running ```sudo raspi-config``` and selecting ```3 Interface Options > P5 I2C > Yes```.

## Installing necessary software

Run the following commands:

1) Make sure the python package manager (pip) is installed:
```bash
sudo apt install python3-pip
```

2) Install git client so we can easily download the project code
```bash
sudo apt install git
```

1) Download the project code
```bash
git clone https://github.com/WhaddaMakers/Whadda_you_see_RPi.git && cd ./Whadda_you_see_RPi
```

4) Install the Text-To-Speech module using our install script:
```bash
sudo chmod +x install_tts.sh && sudo ./install_tts.sh
```

5) Install the required python modules:
```bash
pip3 install -r requirements.txt
```

6) If you are using headphones via the 3.5 mm audio jack, use the raspi-config tool to select the forced headphones audio output
```bash
sudo raspi-config
1 System options > S2 Audio > 1 Headphones
```
## Prepping the connection

It is possible to wire everything up without a breadboard using Male-to-Female jumper wires, although using a breadbord and a Raspberry Pi GPIO extension/breakout board will make the process a lot easier. 

### Connection Tables

| TCS3200 Color sensor | Raspberry Pi |
|:--------------------:|:------------:|
| V | 3V3 |
| G | GND |
| OE | GND |
| LED | GND |
| GND | GND |
| S0 | GPIO 5|
| S1 | GPIO 6 |
| S2 | GPIO 13 |
| S3 | GPIO 19 |
| OUT | GPIO 26 |

| 0.96" OLED | Raspberry Pi |
|:----------:|:------------:|
| VCC | 3V3 |
| GND | GND |
| SCL | SCL1|
| SDA | SDA1|

| Button | Raspberry Pi |
|:------:|:------------:|
| Top right pin | GPIO 20 |
| Bottom left pin | GND |

### Connection Diagram

![](./pictures/fritzing_RPi_bb.png)

## Run the program!
Now it's finally time to test the setup!

If you have an OLED screen installed, you can run the program by entering this command:
```bash
python3 whadda_you_see.py --OLED
```

If you don't have an OLED screen wired up, use this command:
```bash
python3 whadda_you_see.py
```

If you don't want to add the ```python3``` to the command every time to run it, you can make the program executable without it by running the following command:
```bash
sudo chmod +x whadda_you_see.py
```
You can now run the program by using these commands:
```bash
./whadda_you_see.py
OR
./whadda_you_see.py --OLED
```

## Extending/Altering the code

If you want to add and/or change colours you can add additional ```elif``` statements after the line ```color_str = "RED"```:

```python
elif hue_deg > 340 and hue_deg < 356:
        color_str = "RED"
## ADD YOUR OWN COLOUR COMPARE FUNCTIONS HERE ##
# example:
elif hue_deg > 160 and hue_deg < 210:
  color_str = "CYAN/TEAL"
################################################
else:
  color_str = "No valid color detected"
```
Change the numbers in the ```elif``` statement to alter the hue boundaries for which a certain colour name will be set. If you want to get a bit of a "feel" for hue parameters you can use an [HSV colour picker](https://alloyui.com/examples/color-picker/hsv.html) and alter the Hue parameter to see what the corresponding colours are.
