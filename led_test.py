import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [17,27,22,5,6,13,19,26]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
for pin in pins:
    GPIO.output(pin,0)
#GPIO.output(17,0) # 2
#GPIO.output(27,0) # 1
#GPIO.output(22,0) #light 5
#GPIO.output(5,0) #light 7
#GPIO.output(6,0) #light 6
#GPIO.output(13,0) #light 4
#GPIO.output(19,0) #light 3
#GPIO.output(26,0) #light 8
    
def turnOn(pin):
    GPIO.output(pin,1)
def turnOff(pin):
    GPIO.output(pin,0)
def turnAllOff():
    global pins
    for pin in pins:
        GPIO.output(pin,0)
def phase(*argv):
    for arg in argv:
        turnOn(arg)
        
def phaseState(x):
    if x == 0:
        turnAllOff()
    if x == 1:
        phase(27,17,5)
    if x == 2:
        phase(17,19,13,26)
    if x == 3:
        phase(22)
    if x == 4:
        phase(5,6)
    if x == 5:
        phase(13,19,5,6)

#while True:
#    for i in range(5):
#        i += 1
#        phaseState(i)
#        sleep(1.2)
#        turnAllOff()
