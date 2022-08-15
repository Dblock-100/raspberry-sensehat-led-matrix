#get_pixels

#Returned type: List
#Explanation: A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue) representing the currently displayed image.


from sense_hat import SenseHat

sense = SenseHat()
pixel_list = sense.get_pixels()