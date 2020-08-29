# PiTrain LED Service

*Copyright(C) 2020 Johan Thelin*
*Made available under GPLv3 license.*

The PiTrain LED Service is a simple web server letting you control LED lights of a model railway from your phone.

## System Setup

The various GPIOs of a RaspberryPi ZeroW are connected to the LEDs of the model. In ```ledserver.py```, the leds are enumerated and put into an array.

The ```main.py``` contains a Flask server serving ```index.html``` at ```/``` and a tree of ```/api/.../``` routes for controling individual LEDs, groups of LEDs and executing scenes.

The ```index.html``` provides the web front-end to the system through a rudimentary web page.

## Caveats

The server runs on a local LAN and is never exposed to the Internet. There are no security measures and the service is exposed through a Flask app running in debug mode. Use at your own risk!
