"""Manages the function on boot and state of execution"""

from json import load
import pycom, ujson
from station_network.connection_manager import connect, disconnect, connect_to_known_network
from station.sleepmode import put_station_to_sleep

NB_REGISTRATION = 0

def init_station():
    """Initiate the station by reading the conf at boot"""

    global NB_REGISTRATION

    f = open("station/conf.json", 'r')
    conf = load(f)

    pycom.heartbeat(conf["heartbeat"])

    NB_REGISTRATION = conf["nb_registration"]

    # connect(conf["wifi"], conf["password"])
    if not connect_to_known_network(conf["networks"]):
        print("Going back to sleep...")
        shutdown_station(duration=600)

    f.close()



def shutdown_station(duration=600):
    """Disconnect the station and put the station to sleep"""

    print("The station is beeing shutdown for {} seconds".format(duration))

    # Disconnect the current network
    disconnect()

    # Pycom to sleep
    put_station_to_sleep(duration)


def increment_registration():
    """Increment the number of registrations, to keep track to when to send datas to the API"""

    f = open("station/conf.json", 'r')
    temp = load(f)
    f.close()

    temp["nb_registration"] = temp["nb_registration"] + 1
    conf = temp

    f = open("station/conf.json", "w+")
    f.write(ujson.dumps(conf))
    f.close()

def reset_registration():
    """When the datas are beeing send to the API, reset the number of registrations"""

    f = open("station/conf.json", 'r')
    temp = load(f)
    f.close()

    temp["nb_registration"] = 0
    conf = temp

    f = open("station/conf.json", "w+")
    f.write(ujson.dumps(conf))
    f.close()