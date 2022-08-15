#Loads an image file, converts it to RGB format and displays it on the LED matrix. The image must be 8 x 8 pixels in size.

#Parameter  #Type      #Valid values      #Explanation
#file_path  String     Any valid file path.  The file system path to the image file to load.
#redraw     Boolean    True False            Whether or not to redraw the loaded image file on the LED matrix. Defaults to True

from sense_hat import SenseHat

sense = SenseHat()
sense.load_image("space_invader.png")


#Returned type:Lisf
#Explanation: A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue) representing the loaded image after RGB conversion.

from sense_hat import SenseHat

sense = SenseHat()
invader_pixels = sense.load_image("space_invader.png", redraw=False)
