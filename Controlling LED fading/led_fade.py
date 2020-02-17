#**********************#
#This program will control the brightness of led using potentiometer#
#**********************#
# Author : Deeksha & Navya #
# Date   : Jan 25,2020     #
#**********************#

import time
from grovepi import *
#*********************#
# Global Variables    #
#********************#
myLed = 5      #connect LED to digital port 5
angle_sensor = 2     #connect angle sensor to analog port 2
# Initialization
pinMode(myLed, "OUTPUT")   #set the D5 pinMode to output
while (1):
	try:
		#read resistance value from angle sensor
		pot = analogRead(angle_sensor)
		print(pot)
		#control the led using PWM (pulse width modulation)
		analogWrite(myLed, pot / 4)
	except KeyboardInterrupt:
		digitalWrite(myLed, 0)
		print("exiting ...")
		break
	except IOError:
		print("An error has occured.")
