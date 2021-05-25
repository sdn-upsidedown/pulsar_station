"""Manages the data file"""

import os

def register(list_temp, pressure, humidity, light, date):
    """Register a record in the data file"""

    file = open("data/data.txt", "a")
    
    file.write("{\"date\":\"" + date + "\",\"pressure\":" + str(pressure) + ",\"temperature\":" + str(list_temp) + ",\"hygrometry\":" + str(humidity) + ", \"brightness\":" + str(light) + "}")
    file.write("\n")
    
    file.close()
    return True

def print_data_file():
    """Print the content of the data file"""

    file = open("data/data.txt", "r")
    print(file.readlines())
    file.close()
    return True

def delete_data_file() :
    """ Delete the data file """

    os.remove("data/data.txt")