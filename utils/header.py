"""Returns a more user-friendly containers to manipulate sensors"""

from lib.pycoproc_1 import Pycoproc
from lib.LIS2HH12 import LIS2HH12
from lib.SI7006A20 import SI7006A20
from lib.LTR329ALS01 import LTR329ALS01
from lib.MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

py = Pycoproc(Pycoproc.PYSENSE)
dht = SI7006A20(pysense=py)
press = MPL3115A2(pysense=py, mode=PRESSURE)
alt = MPL3115A2(pysense=py, mode=ALTITUDE)
br = LTR329ALS01(pysense=py)