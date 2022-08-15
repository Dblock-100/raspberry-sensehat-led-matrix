#Sets the entire LED matrix to a single colour, defaults to blank / off.

#Parameter  #Type            #Valid values   #Explanation
#colour     Tuple or List     (r, g, b)      A tuple or list containing the RGB (red, green, blue) values of the colour. Each element must be an integer between 0 and 255. Defaults to (0, 0, 0).

#Alternatively, the RGB values can be passed individually:

#Parameter  #Type       #Valid values   #Explanation
#r          Integer      0 - 255        The Red element of the colour.
#g          Integer      0 - 255        The Green element of the colour.
#b          Integer      0 - 255        The Blue element of the colour.

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)

sense.clear()  # no arguments defaults to off
sleep(1)
sense.clear(red)  # passing in an RGB tuple
sleep(1)
sense.clear(255, 255, 255)  # passing in r, g and b values of a colour