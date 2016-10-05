#!/bin/bash
echo "starting IoT Hub Client"

sleep 10

sudo killall python3

cd /home/pi/iothub/smartbuilding

python3 environment.py config_openweather.json&
#python3 environment.py config_envirophat.json&
#python3 environment.py config_sensehat.json&

