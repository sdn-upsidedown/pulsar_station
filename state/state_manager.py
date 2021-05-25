import os

def write_station_state(cpu, temp, volt, perc, date):
    """Register the station state"""

    file = open('state/state.txt', 'a')

    status = "{\"date\":\"" + str(date) + "\",\"cpu\":\"" + str(cpu) + "\",\"station_temperature\":" + str(temp) + ",\"battery_voltage\":" + str(volt) + ",\"battery_percentage\":" + str(perc) + "}\n"
    file.write(status)

    file.close()
    return True

def delete_state_file():
    """Delete the state file"""

    os.remove('state/state.txt')