"""Manages the Internet connection"""

from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.EXT_ANT)

def connect(wifi, auth):
    """Connect the station to a network"""

    # print("Connection to Internet")

    # nets = wlan.scan()

    # for net in nets:
    #     if net.ssid == wifi:
    #         print("Trying to connect to '{}'...".format(net.ssid))

    print("Connection...")

    try:

        wlan.connect(wifi, auth=auth, timeout=5000)

        while not wlan.isconnected():
            machine.idle() # save power while waiting

        return True

    except Exception:
        print("Connection failed, trying to connect to another network...")
        return False

    return False

def connect_to_known_network(networks):
    """Try to connect the station to the first available network"""

    print("Connection to Internet")
    
    list_known_networks = []
    list_password = []

    for n in networks:
        list_known_networks.append(n["wifi"])
        list_password.append(n["password"])

    nets = wlan.scan()


    for net in nets:
        if net.ssid in list_known_networks:
            print("Network foundt, trying to connect to network '{}'...".format(net.ssid))

            if connect(wifi=net.ssid, auth=(net.sec, list_password[list_known_networks.index(net.ssid)])):
                print('Connection succeeded with connection to network {}'.format(net.ssid))
                return True
    
    print("The station could not connect to any network")
    return False

def disconnect():
    """Disconnect the station from the network"""

    print("Station is beeing disconnected")
    wlan.disconnect()
    wlan.deinit()

def is_connected():
    """Check if the station is connected to a network"""

    if wlan.isconnected():
        print("Station connected")
        return True

    print("Station offline")
    return False