#import sense hat libraries
from sense_hat import SenseHat

#make a sense hat
sense = SenseHat()

#load and show the space invader image found at https://raw.githubusercontent.com/astro-pi/python-sense-hat/master/examples/space_invader.png
sense.load_image("trees.png")

#set pixels manually
#sense.set_pixel(0,2, [0,0,255])
#sense.set_pixel(7,4,[255,0,0])
