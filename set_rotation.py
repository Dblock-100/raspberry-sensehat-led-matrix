#If you're using the Pi upside down or sideways you can use this function to correct the orientation of the image being shown.

#Parameter #Type   #Valid values       #Explanation

#r        Integer (0) (9)0 (180) (270) #The angle to rotate the LED matrix though. 0 is with the Raspberry Pi HDMI port facing downwards.

#redraw   Boolean (True) (False)       #Whether or not to redraw what is already being displayed on the LED matrix. Defaults to True

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
# alternatives
sense.rotation = 180