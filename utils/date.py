"""Manages the date"""

import machine
import utime
from time import sleep

def synchronize_date():
    """Synchronize the machine rtc with a server to get the current date"""

    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org")
    while not rtc.synced():
        machine.idle() # save power while waiting

    return rtc

def get_date () :
    """Return the current date"""

    rtc = synchronize_date()
    cd = rtc.now()
    date = "{}-{}-{} {}:{}:{}".format(cd[0],cd[1],cd[2],cd[3]+2,cd[4],cd[5])

    return date