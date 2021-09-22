### SPI Based 1.3" Display
This repo holds code, instructions and BOMs for the Waveshare 1.3" TFT. 

The primary source for information is: https://www.waveshare.com/wiki/1.3inch_LCD_HAT


Configure a new RPi, enabling SPI

    sudo raspi-config
    Choose Interfacing Options -> SPI -> Yes  to enable SPI interface
    sudo reboot

Get the software, BCM2835 libraries

    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
    tar zxvf bcm2835-1.68.tar.gz 
    cd bcm2835-1.68/
    sudo ./configure && sudo make && sudo make check && sudo make install

Install Python libraries

    sudo apt-get update
    sudo apt-get install ttf-wqy-zenhei
    sudo apt-get install python-pip 
    sudo pip install RPi.GPIO
    sudo pip install spidev

Get the example code

    sudo apt-get install p7zip-full -y
    wget https://www.waveshare.com/w/upload/b/bd/1.3inch_LCD_HAT_code.7z
    7z x 1.3inch_LCD_HAT_code.7z -r -o./1.3inch_LCD_HAT_code
    sudo chmod 777 -R 1.3inch_LCD_HAT_code
    cd 1.3inch_LCD_HAT_code

Compile and install

    cd c
    make clean
    make
    sudo ./main

## Sample code
1. I have written an application for NMEA heading sentences (heading_display.py)

![](HeadingSensor.jpg)