#gamma_reset
#A function to reset the gamma lookup table to default, ideal if you've been messing with it and want to get it back to a default state.

import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255, 127, 0)
time.sleep(2)
sense.gamma = [0] * 32  # Will turn the LED matrix off
time.sleep(2)
sense.gamma_reset()