"""Functions to analyze the station status"""

import machine
from lib.pycoproc_1 import Pycoproc

def cpu_frequency():
    return machine.freq()

def station_id():
    return machine.unique_id()

def station_temp():
    return machine.temperature()

def battery_voltage():
    py = Pycoproc(Pycoproc.PYSENSE)
    return py.read_battery_voltage()

def battery_percentage(voltage):
    vmax = 4.2
    vmin = 3.3
    return (voltage - vmin / (vmax - vmin))*100