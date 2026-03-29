from temperaturedb import TemperatureDB
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/rack", methods=["GET"])
def get_garage_data():
    conn = TemperatureDB("temphistory.db")
    garage_data = conn.readLastTemp()
    return garage_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
