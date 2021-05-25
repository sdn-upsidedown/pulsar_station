import pycom
from time import sleep

RED    = 0xFF0000
BLUE   = 0x0000FF
GREEN  = 0xff00
YELLOW = 0xFFFF00
ORANGE = 0xFF5733
PURPLE = 0xFF00FF
WHITE  = 0xFFFFFF
PINK   = 0xFFA9FB

color_list = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE, PINK]

def led_to(color):
    return pycom.rgbled(color)

def blink(cl=color_list):
    for c in cl:
        led_to(c)
        sleep(1)

def lgbt():
    blink([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])