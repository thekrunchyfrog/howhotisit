from datetime import datetime
from temperaturedb import TemperatureDB
import adafruit_dht
import board
import time


def get_garage_data(iterations):
    tempList = []

    for i in range(0, iterations):
        try:
            weather = readTemp()
        except RuntimeError as err:
            continue
        tempList.append(weather)
        time.sleep(2)

    garage_data = tempList[1]
    return garage_data


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

    return {"temperature_f": temperature_f, "temperature_c": temperature_c, "humidity": humidity}


def main():
    db_file = "/home/rich/Repos/howhotisit/temphistory.db"
    curr_datetime = datetime.now()
    data = get_garage_data(3)
    conn = TemperatureDB(db_file)
    conn.createTemp(curr_datetime, data["temperature_c"], data["temperature_f"], data["humidity"], "rack")
    conn.close()


if __name__ == "__main__":
    main()
