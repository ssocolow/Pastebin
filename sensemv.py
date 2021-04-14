#import sense hat libraries
from sense_hat import SenseHat
#import sleep
from time import sleep

#make a sense hat
sense = SenseHat()

#set up the sensors
sense.set_imu_config(True, True, True)

#print orientation in radians, direction of north from magnetometer in degrees, and the acceleration from accelerometer
while True:
  print("Orientation: " + str(sense.orientation_radians))
  print("North: " + str(sense.get_compass()))
  print("Acceleration " + str(sense.accel))
  sleep(1)

