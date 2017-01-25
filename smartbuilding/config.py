import json

class Config():

    @property
    def sampleRateInSeconds(self):
        return self._sampleRate

    @sampleRateInSeconds.setter
    def sampleRateInSeconds(self, value):
        try:
            self._sampleRate = float(value)

            if self._sampleRate < 0.1:
                self._sampleRate = 0.1
            if self._sampleRate > 100000:
                self._sampleRate = 100000

        except:
            self._sampleRate = self._sampleRate

    def config_defaults(self):
        print('Loading default config settings')

        self.sensor = __import__('sensor_openweather') 
        self.hubAddress = 'IoTCampAU.azure-devices.net'
        self.deviceId = 'mqttwindows'
        self.sharedAccessKey= 'YdPKYydqxdkZTNqNzFO4mGajb15vjJRibL3tUCdX4B0='
        self.owmApiKey = 'c204bb28a2f9dc23925f27b9e21296dd'
        self.owmLocation = 'Melbourne, AU'

    def config_load(self, configFile):
        #global sensor, hubAddress, deviceId, sharedAccessKey, owmApiKey, owmLocation
        try:
            print('Loading {0} settings'.format(configFile))

            config_data = open(configFile)
            config = json.load(config_data)

            self.sensor = __import__(config['SensorModule']) 
            self.hubAddress = config['IotHubAddress']
            self.deviceId = config['DeviceId']
            self.sharedAccessKey = config['SharedAccessKey']
            self.owmApiKey = config['OpenWeatherMapApiKey']
            self.owmLocation = config['OpenWeatherMapLocationId']
        except:
            self.config_defaults()

    def __init__(self, configFile):
        self.sampleRateInSeconds = 12 #set publishing rate in seconds. every 12 seconds good for an 8000 msg/day free Azure IoT Hub
        self.iotHubMode = True
        self.config_load(configFile)