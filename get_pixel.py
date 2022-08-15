#Parameter  #Type      #Valid values   #Explanation
#x          Integer     0 - 7          0 is on the left, 7 on the right.
#y          Integer     0 - 7          0 is at the top, 7 at the bottom.

#Returned Type: List
#Explanation: Returns a list of [R, G, B] representing the colour of an individual LED matrix pixel at the specified X-Y coordinate.

from sense_hat import SenseHat

sense = SenseHat()
top_left_pixel = sense.get_pixel(0, 0)