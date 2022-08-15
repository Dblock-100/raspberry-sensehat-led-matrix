#Sets an individual LED matrix pixel at the specified X-Y coordinate to the specified colour.

#Parameter #Type    #Valid values      #Explanation
#x         Integer      0 - 7          0 is on the left, 7 on the right.
#y         Integer      0 - 7          0 is at the top, 7 at the bottom.
#Colour can either be passed as an RGB tuple:

#Parameter #Type          #Valid values    #Explanation
#pixel     Tuple or List   (r, g, b)        Each element must be an integer between 0 and 255.

#Or three separate values for red, green and blue:
#Parameter  #Type          #Valid values     #Explanation
#r          Integer          0 - 255         The Red element of the pixel.
#g          Integer          0 - 255         The Green element of the pixel.
#b          Integer          0 - 255         The Blue element of the pixel.

from sense_hat import SenseHat

sense = SenseHat()

# examples using (x, y, r, g, b)
sense.set_pixel(0, 0, 255, 0, 0)
sense.set_pixel(0, 7, 0, 255, 0)
sense.set_pixel(7, 0, 0, 0, 255)
sense.set_pixel(7, 7, 255, 0, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# examples using (x, y, pixel)
sense.set_pixel(0, 0, red)
sense.set_pixel(0, 0, green)
sense.set_pixel(0, 0, blue)