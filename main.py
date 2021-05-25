from time import sleep

from data.data_manager import *
from sensors.sens_func import *
from station.led import *
from station.manager import shutdown_station, NB_REGISTRATION, increment_registration, reset_registration
from station_network.api_manager import *
from station_network.connection_manager import *
from utils.date import get_date
from utils.interface.console import report
from state.stats import *
from state.state_manager import write_station_state


# Get the current temperature in an array to get a more precise temperature
def temperature(precision=5, interval=2):
    """Get the current temperature in an array to get a more precise temperature"""
    li_temp = []

    for i in range(precision):
        li_temp.append(get_temperature())
        sleep(interval)

    return li_temp


if __name__ == "__main__":
    print("Station is now running\n")

    # Fetch the current datas

    # temp = temperature()
    # press = get_pressure() * 1000
    # hum = get_humidity()
    # li = get_light()[0]
    date = get_date()
    cpu = cpu_frequency()
    s_temp = station_temp()
    vol = battery_voltage()
    perc = battery_percentage(vol)

    # # register the data

    # register(temp, press, hum, li, date)
    # increment_registration()

    # Register the station state

    write_station_state(cpu, s_temp, vol, perc, date)

    # # Every hour (6 datas) the datas are send to the api

    # if NB_REGISTRATION > 5:
    #     print("Send data to api...")
        
    #     if send_data_to_api():
    #         print("Data transfer succeeded")
    #         reset_registration()

    # # Put the station back to sleep

    # shutdown_station()

    disconnect()            # For test purposes