import adafruit_dht
import board
import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/garage", methods=["GET"])
def get_garage_data():
    tempList = []

    for x in range(0, 3):
        try:
            weather = readTemp()
        except RuntimeError as err:
            continue
        tempList.append(weather)
        time.sleep(2)

    garage_data = tempList[1]
    return jsonify(garage_data)

def readTemp():
    dht_device = adafruit_dht.DHT22(board.D4)
    
    temperature_c = None
    humidity = None
        
    while temperature_c is None:
        temperature_c = dht_device.temperature
        
    temperature_f = temperature_c * (9 / 5) + 32
        
    while humidity is None:
        humidity = dht_device.humidity
        
    dht_device.exit()
        
    return {"temperature": temperature_f, "humidity": humidity}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

