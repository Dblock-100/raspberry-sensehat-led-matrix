#Flips the image on the LED matrix horizontally.

#Parameter #Type   #Valid values       #Explanation

#redraw   Boolean (True) (False)       #Whether or not to redraw what is already being displayed on the LED matrix. Defaults to True

#Returned type: List
#Explanation: A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue) representing the flipped image.

from sense_hat import SenseHat

sense = SenseHat()
sense.flip_h()