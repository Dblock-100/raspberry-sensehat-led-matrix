#Updates the entire LED matrix based on a 64 length list of pixel values.

#Parameter  #Type    #Valid values       #Explanation
#pixel_list List     [[R, G, B] * 64]    A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue). Each R-G-B element must be an integer between 0 and 255.

from sense_hat import SenseHat

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)