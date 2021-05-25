def report(temperature, humidity, dew_point, air_pressure, alt):
    """Clean print of the datas in parameter"""
    
    # now = time.localtime().tm_mday + "/" + time.localtime().tm_mon() + "/" + time.localtime().tm_year() + " " + time.localtime().tm_hour() + ":" + time.localtime().tm_min() + ":" + time.localtime().tm_sec()
    out = "\n* Données : \n"
    out += "\tTemperature  :    " + str(temperature)  + "°C\n"
    out += "\tHumidity     :    " + str(humidity)     + "\n"
    out += "\tDew point    :    " + str(dew_point)     + "\n"
    out += "\tAir pressure :    " + str(air_pressure) + "P\n"
    out += "\tAltitude     :    " + str(alt)          + "m\n"

    print(out)