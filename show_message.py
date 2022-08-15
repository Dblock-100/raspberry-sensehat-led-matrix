#Scrolls a text message from right to left across the LED matrix and at the specified speed, in the specified colour and background colour.


#Parameter       #Type       #Valid values              #Explanation
#text_string     String      Any text string            The message to scroll.
#scroll_speed    Float       Any floating point number. The speed at which the text should scroll. This value represents the time paused for between shifting the text to the left by one column of pixels. Defaults to 0.1
#text_colour     List        [R, G, B]                  A list containing the R-G-B (red, green, blue) colour of the text. Each R-G-B element must be an integer between 0 and 255. Defaults to [255, 255, 255] white.
#back_colour     List        [R, G, B]                  A list containing the R-G-B (red, green, blue) colour of the background. Each R-G-B element must be an integer between 0 and 255. Defaults to [0, 0, 0] black / off.

from sense_hat import SenseHat

sense = SenseHat()
sense.show_message("One small step for Pi!", text_colour=[255, 0, 0])

