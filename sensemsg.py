#import sense hat libraries
from sense_hat import SenseHat

#make a sense hat
sense = SenseHat()

#have a color
color = (20, 190, 230)

#show the message with the chosen text color, background color, and scroll speed
sense.show_message("Hello, World!", text_colour = color, back_colour = (163,20,200), scroll_speed = 0.1)
