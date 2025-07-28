import adafruit_dht
import board
from time import sleep


class Thermometer:

    def __init__(self):
        self.dht_device = adafruit_dht.DHT22(board.D4)
    
    def readTemp(self):
        temperature_c = None
        humidity = None
        
        while temperature_c is None:
            temperature_c = self.dht_device.temperature
        
        temperature_f = temperature_c * (9 / 5) + 32
        
        while humidity is None:
            humidity = self.dht_device.humidity
        
        return {"temperature": temperature_f, "humidity": humidity}

    def close(self):
        self.dht_device.exit()
