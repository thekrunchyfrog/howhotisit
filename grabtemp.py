from datetime import datetime
from temperaturedb import TemperatureDB
import random


curr_datetime = datetime.now()
rand_temp = random.uniform(-10.5, 100.7)
rand_humid = random.uniform(0.00, 100.0)

conn = TemperatureDB("temphistory.db")
conn.recordTemp(curr_datetime, rand_temp, rand_humid, "garage")
conn.close()
