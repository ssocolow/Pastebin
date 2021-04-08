#spinny light game with raspberry pi and leds
#made by Simon Socolow in March/April 2021

#use RPi.GPIO and time libraries
import RPi.GPIO as GPIO
from time import sleep

#function that turns off all lights
def off():
    for i in pins:
        if i == 17:
            GPIO.output(i, True)
        else:
            GPIO.output(i, False)

#function that turns on all lights
def on():
    for i in pins:
        if i == 17:
            GPIO.output(i, False)
        else:
            GPIO.output(i, True)

#instructions
print("Spinny game!  Try to stop the light on the big led!  Survive as many rounds as possible!")
print("Getting the red led 3 times in a row gives you back a life, getting the red led makes the light go faster")
print("Getting other leds makes you lose a life and makes the light go slower")
print("GOOD LUCK!")

#initialize the led pins list, the score, the round, the lives, the number of wins in a streak, and the reversed pins list
pins = [17, 21, 23, 20, 24, 12, 25, 18, 4]
score = 0
rnd = 0
lives = 5
rwins = 0
rpins = list(reversed(pins))

#set GPIO mode and set the button on pin 26 as an input
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

#set the starting time for turning on and off leds
t = 0.05

#set the stopped game state as False to start
stopped = False

#setup all the pins in the pins list (which has all the leds) to outputs
for i in pins:
    GPIO.setup(i, GPIO.OUT)

#turn off all leds
off()

#function to do one round
def spin():
    #use global variables
    global stopped
    global t
    #do this until stopped
    while True:
      if stopped == False:
          #for all of the pins turn them on then turn them off, sleeping a time t in between and after
          for i in pins:
              #diffused rgb led turns on differently than others
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
              #if the button is pressed
              if GPIO.input(26) == True:
                  #use global variables
                  global score
                  global rnd
                  global lives
                  global rwins
                  #set stopped as true
                  stopped = True
                  #increment the round number
                  rnd += 1
                  #if the light stopped on the rgb led
                  if i == 17:
                      #global t
                      GPIO.output(i, False)
                      score += 1
                      #make the time between led switches faster
                      t -= 0.005
                      #increase streak variable
                      rwins += 1
                      #if streak is greater than 3
                      if rwins >= 3:
                        #get an extra life
                        lives += 1
                        print("You got a life back!")
                      #print information
                      print("Lives: " + str(lives) +" Round "+ str(rnd) + " time: " + str(t))
                  #if the led is not the rgb led
                  else:
                      #global t
                      GPIO.output(i, True)
                      #lose a life
                      lives -= 1
                      #set streak to 0
                      rwins = 0
                      #make the game easier
                      t += 0.005
                      #print information
                      print("Lives: " + str(lives) +" Round "+ str(rnd) + " time: " + str(t))
                  #wait
                  sleep(1)
                  #turn all leds off
                  off()
                  #print("done")
                  #set stopped back to false
                  stopped = False
                  #do the effects
                  effects()

#function for effects
def effects():
    #do an effect which runs the lights from different directions around the circle
    for i in range(len(pins)):
        if i == 0:
            GPIO.output(17, False)
        else:
            GPIO.output(pins[i], True)
            GPIO.output(rpins[i - 1], True)
        sleep(0.05)
        off()
    #blink rgb led twice
    GPIO.output(17, False)
    sleep(0.5)
    GPIO.output(17, True)
    sleep(0.5)
    GPIO.output(17, False)
    sleep(0.5)
    off()
    global rnd
    #if the round is 10 print out a compliment
    if rnd == 10:
      print("You got to round 10!")
      on()
      sleep(0.5)
      off()
      sleep(0.5)
    global lives
    #as long as you have greater than or equal to one life, play the game again
    if lives >= 1:
      spin()
    #otherwise, you lose
    else:
      #print info
      print("Good job! You got to round " + str(rnd))
      #quit from code
      quit()


#old effects function 

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
        
#do spin 
spin()
#for i in range(100):
#    spin()

#helper functions, some old and not used
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
