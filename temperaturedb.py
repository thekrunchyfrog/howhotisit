import sqlite3


class TemperatureDB:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()

    def recordTemp(self, timestamp, temperature, humidity, location):
        self.cursor.execute(
            f"INSERT INTO history (temperature, humidity, timestamp, location) VALUES ('{temperature}', '{humidity}', '{timestamp}', '{location}')"
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
