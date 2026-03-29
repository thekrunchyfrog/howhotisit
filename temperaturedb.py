import json
import sqlite3


class TemperatureDB:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def createTemp(self, timestamp, temp_c, temp_f, humidity, location):
        self.cursor.execute(
            f"INSERT INTO history (temperature_c, temperature_f,  humidity, timestamp, location) VALUES ('{temp_c}', '{temp_f}', '{humidity}', '{timestamp}', '{location}')"
        )
        self.conn.commit()

    def readLastTemp(self):
        self.cursor.execute("select * from history where location='rack' order by id DESC LIMIT 1")
        results = self.cursor.fetchone()
        columns = [col[0] for col in self.cursor.description]
        data = dict(zip(columns, results))
        return json.dumps(data, indent=2)
