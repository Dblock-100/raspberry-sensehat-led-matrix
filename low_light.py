#Toggles the LED matrix low light mode, useful if the Sense HAT is being used in a dark environment.

import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255, 255, 255)
sense.low_light = True
time.sleep(2)
sense.low_light = False