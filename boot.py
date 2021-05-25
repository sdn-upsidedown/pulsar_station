# boot.py -- run on boot-up
from station.manager import init_station
import machine

print("Station is starting...")

init_station()                  # Initiate the station

machine.main("main.py")         # Returning to the main