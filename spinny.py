#spinny light game with raspberry pi and leds
#made by Simon Socolow in March/April 2021
import RPi.GPIO as GPIO
from time import sleep

def off():
    for i in pins:
        if i == 17:
            GPIO.output(i, True)
        else:
            GPIO.output(i, False)

def on():
    for i in pins:
        if i == 17:
            GPIO.output(i, False)
        else:
            GPIO.output(i, True)

print("Spinny game!  Try to stop the light on the big led!  Survive as many rounds as possible!")
print("Getting the red led 3 times in a row gives you back a life, getting the red led makes the light go faster")
print("Getting other leds makes you lose a life and makes the light go slower")
print("GOOD LUCK!")
pins = [17, 21, 23, 20, 24, 12, 25, 18, 4]
score = 0
rnd = 0
lives = 5
rwins = 0
rpins = list(reversed(pins))
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
t = 0.05
stopped = False

for i in pins:
    GPIO.setup(i, GPIO.OUT)

off()
def spin():
    global stopped
    global t
    while True:
      if stopped == False:
          for i in pins:
              if i == 17:
                  GPIO.output(i, False)
                  sleep(t)
                  GPIO.output(i, True)
                  sleep(t)
              else:
                  GPIO.output(i, True)
                  sleep(t)
                  GPIO.output(i, False)
                  sleep(t)
              if GPIO.input(26) == True:
                  global score
                  global rnd
                  global lives
                  global rwins
                  stopped = True
                  rnd += 1
                  if i == 17:
                      #global t
                      GPIO.output(i, False)
                      score += 1
                      t -= 0.005
                      rwins += 1
                      if rwins >= 3:
                        lives += 1
                        print("You got a life back!")
                      print("Lives: " + str(lives) +" Round "+ str(rnd) + " time: " + str(t))
                  else:
                      #global t
                      GPIO.output(i, True)
                      lives -= 1
                      rwins = 0
                      t += 0.005
                      print("Lives: " + str(lives) +" Round "+ str(rnd) + " time: " + str(t))
                  sleep(1)
                  off()
                  #print("done")
                  stopped = False
                  effects()

def effects():
    for i in range(len(pins)):
        if i == 0:
            GPIO.output(17, False)
        else:
            GPIO.output(pins[i], True)
            GPIO.output(rpins[i - 1], True)
        sleep(0.05)
        off()
    GPIO.output(17, False)
    sleep(0.5)
    GPIO.output(17, True)
    sleep(0.5)
    GPIO.output(17, False)
    sleep(0.5)
    off()
    global rnd
    if rnd == 10:
      print("You got to round 10!")
      on()
      sleep(0.5)
      off()
      sleep(0.5)
    global lives
    if lives >= 1:
      spin()
    else:
      print("Good job! You got to round " + str(rnd))
      quit()

                    
                
#def effects(n):
#    if n == 17:
#        GPIO.output(n, True)
#        sleep(0.5)
#    else:
#        GPIO.output(n, False)
#        sleep(0.5)
#    for i in range(len(pins)):
#        p = len(pins) - 1 - i
#        print(p)
#        if i == 0:
#            GPIO.output(17, False)
#            sleep(0.5)
#            GPIO.output(17, True)
#            print('hi')
#        else:
#            GPIO.output(pins[p], True)
#            sleep(0.5)
#            GPIO.output(pins[p], False)
        
        
spin()
#for i in range(100):
#    spin()
def blue():
    GPIO.output(26, False)
    GPIO.output(5, True)
    GPIO.output(19, True)
def red():
    GPIO.output(26, True)
    GPIO.output(5, False)
    GPIO.output(19, True)
def green():
    GPIO.output(26, True)
    GPIO.output(5, True)
    GPIO.output(19, False)
def off():
    for i in pins:
        if i == 17:
            GPIO.output(i, True)
        else:
            GPIO.output(i, False)
def on():
    GPIO.output(26, True)
    GPIO.output(5, True)
    GPIO.output(19, True)
def pink():
    GPIO.output(26, True)
    GPIO.output(5, False)
    GPIO.output(19, False)
