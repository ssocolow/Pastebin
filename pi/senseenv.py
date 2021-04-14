#import sense hat libraries
from sense_hat import SenseHat

#make a sense hat
sense = SenseHat()

#get environmental data and print them
#Humidity is in relative humidity as percentage
#Temperature is by default in degrees C
#Pressure is in millibars
print("Humidity " + str(sense.get_humidity()))
print("Tempurature " + str(sense.temp) + "C " + str(sense.temp * (9/5) + 32) + "F")
print("Pressure " + str(sense.get_pressure()))

#show the temp in degrees C on the pixels
sense.show_message(str(sense.temp)[0:4] + "C")
