#import sense hat libraries
from sense_hat import SenseHat
from time import sleep
from sense_tools import Sense_BOARD
import random

#make a sense hat
sense = SenseHat()
sense.clear()
sense.set_rotation(180)

b = Sense_BOARD(sense)
x = 3
y = 0
c = 0
t = 0.03
lives = 3
asteroids = []
first = True

#if pitch is > 20 it is pitched left, if it is < 340 it is right
while True:
  c += 1
  sleep(t)
  #sense.clear() #takes too long to clear all pixels
  pitch = sense.orientation["pitch"]
  if first:
    b.set_pixel(x,y,[0,0,255])
    first = False
  if pitch > 20 and pitch < 100 and x < 7:
    b.set_pixel(x,y,[0,0,0])
    x = x + 1
    b.set_pixel(x,y,[0,0,255])
  elif pitch < 340 and pitch > 300 and x > 0:
    b.set_pixel(x,y,[0,0,0])
    x = x - 1
    b.set_pixel(x,y,[0,0,255])
  else:
    pass

#  if lives == 3:
#    sense.set_pixel(3,7,[255,255,255])
#    sense.set_pixel(4,7,[255,255,255])
#    sense.set_pixel(5,7,[255,255,255])
#  elif lives == 2:
#    sense.set_pixel(4,7,[255,255,255])
#    sense.set_pixel(5,7,[255,255,255])
#  elif lives == 1:
#    sense.set_pixel(4,7,[255,255,255])
#  elif lives == 0:
#    sense.set_pixel(4,7,[255,0,0])
#    quit()

  if c % 10 == 0:
    asteroids.append(random.choice([[1,7],[2,7]]))
    if asteroids[-1][0] == 1:
      b.set_pixel(0,7,[255,0,0])
      b.set_pixel(1,7,[255,0,0])
      b.set_pixel(2,7,[255,0,0])
      b.set_pixel(3,7,[255,0,0])
    else:
      b.set_pixel(4,7,[255,0,0])
      b.set_pixel(5,7,[255,0,0])
      b.set_pixel(6,7,[255,0,0])
      b.set_pixel(7,7,[255,0,0])


  
  if c % 3 == 0:
    for ast in asteroids:
      if ast[1] == 0:
        asteroids.remove(ast)
        if ast[0] == 1:
          b.set_pixel(0,0,[0,0,0])
          b.set_pixel(1,0,[0,0,0])
          b.set_pixel(2,0,[0,0,0])
          b.set_pixel(3,0,[0,0,0])
        else:
          b.set_pixel(4,0,[0,0,0])
          b.set_pixel(5,0,[0,0,0])
          b.set_pixel(6,0,[0,0,0])
          b.set_pixel(7,0,[0,0,0])
 
      elif ast[0] == 1:
        b.set_pixel(0,ast[1],[0,0,0])
        b.set_pixel(1,ast[1],[0,0,0])
        b.set_pixel(2,ast[1],[0,0,0])
        b.set_pixel(3,ast[1],[0,0,0])
        ast[1] -= 1
        b.set_pixel(0,ast[1],[255,0,0])
        b.set_pixel(1,ast[1],[255,0,0])
        b.set_pixel(2,ast[1],[255,0,0])
        b.set_pixel(3,ast[1],[255,0,0])
      else:
        b.set_pixel(4,ast[1],[0,0,0])
        b.set_pixel(5,ast[1],[0,0,0])
        b.set_pixel(6,ast[1],[0,0,0])
        b.set_pixel(7,ast[1],[0,0,0])
        ast[1] -= 1
        b.set_pixel(4,ast[1],[255,0,0])
        b.set_pixel(5,ast[1],[255,0,0])
        b.set_pixel(6,ast[1],[255,0,0])
        b.set_pixel(7,ast[1],[255,0,0])
      if ast[0] == 1 and x < 4 and ast[1] == 0:
        b.set_pixel(x,y,[0,255,0])
        b.update_board()
        print(c)
        lives -= 1
        quit()
      if ast[0] == 2 and x > 3 and ast[1] == 0:
        b.set_pixel(x,y,[0,255,0])
        b.update_board()
        print(c)
        lives -= 1
        quit()
  if c % 120 == 0:
    t = t - 0.01
  #b.print_board()
  b.update_board()


