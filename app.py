import time
from thermometer import Thermometer
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/garage", methods=["GET"])
def get_garage_data():
    tempList = []

    garage = Thermometer()

    for x in range(0, 3):
        try:
            weather = garage.readTemp()
        except RuntimeError as err:
            continue
        tempList.append(weather)
        time.sleep(2)
    garage.close()

    # Example data for the garage, replace with real data fetching logic
    garage_data = tempList[1]
    return jsonify(garage_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

