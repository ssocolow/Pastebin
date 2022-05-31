#this is meant to be used with a raspberry pi that is hooked up to a buzzer and LED

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.OUT)

connected = 0
unconnected = 0
ready = False
GPIO.output(21, True)
start = time.time()
rtdelay = random.random() * 5 + 3

while True:
    t = time.time()
    if t - start > rtdelay:
        if not ready:
            GPIO.output(21, False)
            ready = True
        if GPIO.input(26):
            print("Buzzer 1 wins you took: " + str(t - start - rtdelay) + " seconds")
            break
        if GPIO.input(20):
            print("Buzzer 2 wins you took: " + str(t - start - rtdelay) + " seconds")
            break
    if GPIO.input(26):
        print("buzzer 1 buzzed early")

    if GPIO.input(20):
        print("buzzer 2 buzzed early")

#for i in range(10000):
#    time.sleep(0.001)
#    if i == 5000:
#        print("go")
#        ready = True
#        GPIO.output(21, False)
#        start = time.time()
#
#    t = GPIO.input(26)
#    if ready and GPIO.input(26):
#        end = time.time()
#        print("you took: " + str(end - start) + " seconds")
#        break
#    if t:
#        connected += 1
#    else:
#        unconnected += 1
#    print("pushed: " + str(connected) + "        " + "open: " + str(unconnected))
#    print(time.time())
