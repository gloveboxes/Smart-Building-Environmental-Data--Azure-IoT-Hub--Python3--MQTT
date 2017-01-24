import sys
import owm 
from envirophat import light, weather, leds

class Sensor():

    msg_txt = "{\"Geo\":\"%s\",\"Humidity\":%d,\"HPa\":%d,\"Celsius\": %.2f,\"Light\":%d,\"Id\":%d}"
   
    def __init__(self, owmApiKey, owmLocation='Sydney, au', cacheSeconds=60):
        self.sensorLocation = owmLocation
        self.id = 0


    def measure(self):
        leds.on()

        self.id += 1
        humidity = 50

        ## normalise light to something of 100%
        lightLevel = light.light();
        if lightLevel > 1024:
            lightLevel = 1024            
        lightLevel = lightLevel * 100 / 1024        

        json = self.msg_txt % (self.sensorLocation, humidity, round(weather.pressure()/100,2),  round(weather.temperature(),2), lightLevel, self.id)
        
        leds.off()
        return json