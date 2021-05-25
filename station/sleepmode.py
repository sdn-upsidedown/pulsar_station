"""Manages the sleep mode of the station"""

from lib.pycoproc_1 import Pycoproc

def put_station_to_sleep(duration=60000):
    """Put the station to sleep for <duration>"""

    print("Setting up sleep duration...")
    Pycoproc(Pycoproc.PYSENSE).setup_sleep(duration)    # Setup the sleep duration

    print("Sleep mode activated")
    Pycoproc(Pycoproc.PYSENSE).go_to_sleep()            # shutdown the station