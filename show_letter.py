#Displays a single text character on the LED matrix.

#Parameter    #Type    #Valid value                  #Explanplan
#s            String   A text string of length 1.    The letter to show.
#text_colour  List     [R, G, B]                     A list containing the R-G-B (red, green, blue) colour of the letter. Each R-G-B element must be an integer between 0 and 255. Defaults to [255, 255, 255] white.
#back_colour  List     [R, G, B]                     A list containing the R-G-B (red, green, blue) colour of the background. Each R-G-B element must be an integer between 0 and 255. Defaults to [0, 0, 0] black / off.

import time
from sense_hat import SenseHat

sense = SenseHat()

for i in reversed(range(0,10)):
    sense.show_letter(str(i))
    time.sleep(1)
