from sense_hat import SenseHat
from time import sleep
from sense_tools import Sense_BOARD
import random

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

b = Sense_BOARD(sense)

x = 3
y = 3
vx = 1

while True:
  sleep(0.05)
  if x == 7:
    vx = -1
  elif x == 0:
    vx = 1

  b.set_pixel(x,y,[0,0,0])
  x += vx
  b.set_pixel(x,y,[100,200,255])
  b.update_board()
