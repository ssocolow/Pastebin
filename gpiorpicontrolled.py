import RPi.GPIO as GPIO
from time import sleep

p1 = 12
p2 = 16
p3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)
GPIO.setup(p3,GPIO.OUT)

time = float(input("enter a delay time: "))
order = int(input("enter an order number: "))

def tp1():
	GPIO.output(p1, True)
	sleep(time)
	GPIO.output(p1, False)

def tp2():
	GPIO.output(p2, True)
	sleep(time)
	GPIO.output(p2, False)

def tp3():
	GPIO.output(p3, True)
	sleep(time)
	GPIO.output(p3, False)


while True:
	if order == 0:
		tp1()
		tp2()
		tp3()
	if order == 1:
		tp2()
		tp1()
		tp3()
	if order == 2:
		tp2()
		tp3()
		tp1()
	if order == 3:
		tp3()
		tp2()
		tp1()
	if order == 4:
		tp3()
		tp1()
		tp2()
	GPIO.output(p1, False)
	GPIO.output(p2, False)
	GPIO.output(p3, False)
	sleep(time)
