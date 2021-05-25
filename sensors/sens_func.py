"""Functions to fetch the current weather data"""

from utils.header import press, alt, dht, br

def get_pressure():
    return press.pressure()

def get_temperature():
    return dht.temperature()

def get_altitude():
    return alt.altitude()

def get_humidity():
    return dht.humidity()

def get_dewpoint():
    return dht.dew_point()

def get_light():
    return br.light()