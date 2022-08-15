# For advanced users. Most users will just need the low_light Boolean property above.
#The Sense HAT python API uses 8 bit (0 to 255) colours for R, G, B.
#When these are written to the Linux frame buffer they're bit shifted into RGB 5 6 5.
#The driver then converts them to RGB 5 5 5 before it passes them over to the ATTiny88 AVR for writing to the LEDs.
# 
# The gamma property allows you to specify a gamma lookup table for the final 5 bits of colour used.
#The lookup table is a list of 32 numbers that must be between 0 and 31.
#The value of the incoming 5 bit colour is used to index the lookup table and the value found at that position is then written to the LEDs.

#Type             #Valid values                                 #Explanation
#Tuple or List    length 32 containing Integers between 0-31    Gamma lookup table for the final 5 bits of colour

import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255, 127, 0)

print(sense.gamma)
time.sleep(2)

sense.gamma = reversed(sense.gamma)
print(sense.gamma)
time.sleep(2)

sense.low_light = True
print(sense.gamma)
time.sleep(2)

sense.low_light = False