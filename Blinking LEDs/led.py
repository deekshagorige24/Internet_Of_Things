import time
from grovepi import *

red = 2
blue = 3
green = 4
pinMode(red, "OUTPUT")
pinMode(blue, "OUTPUT")
pinMode(green, "OUTPUT")
while True:
	try:
       		digitalWrite(red, 1)
       		print("ON")
		digitalWrite(green, 1)
		print("ON")
		time.sleep(0.5)
		digitalWrite(blue, 0)
                print("ON")
		time.sleep(0.5)
		digitalWrite(red, 0)
                print("OFF")
                digitalWrite(green, 0)
                print("OFF")
		time.sleep(0.5)
                digitalWrite(blue, 1)
                print("ON")
		time.sleep(0.5)

	except KeyboardInterrupt:
		digitalWrite(red, 0)
		digitalWrite(blue, 0)
		digitalWrite(green, 0)
		break

	except IOError:
		print("Error")

