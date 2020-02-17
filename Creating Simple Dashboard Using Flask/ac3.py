1# TCSS573 : IoT
# Feb 01, 2020
# Group 8
# Import flask libraries
# for more details on flask, go to
# https://www.tutorialspoint.com/flask/index.htm
from flask import Flask, render_template
from grovepi import *
import time
import math

# flask constructor for taking the current module
# as an argument
app = Flask(__name__)

# read the temperature sensor from D3 port
sensor = 3
# read the ultrasonic range values from D4 port
ultra = 4
# read the buzzer sensor from D8 port
buzzer = 8
# set the D8 pinMode to output
pinMode(buzzer, "OUTPUT")
# set the D4 pinMode to output
pinMode(ultra, "INPUT")

# *************************************
# Routing in Flask
# *************************************
# flask uses a routing technique for
# enabling the user to remember URLs
# of applications (eg. similar to REST)
# You can then access the page directly
# with no further navigation


# route the getTemp function
# this function will be used
# when we call the this file
# from the AJAX script in the
# HTML file. That is, when the
# setInterval in from Google Chart
# elapses, call this function
# it simply returns the temperature
@app.route("/getTemp")
def getTemp():
  [temp, hum] = dht(sensor, 0)
#  print(temp)
  return str(temp)


# route the buzz function
# this function will be used
# when we call this file from
# the AJAX script in the HTML
# file. That is, when the 
# setInterval from Google chart
# elapses, call this function
# it simply returns the 'motion'
@app.route("/buzz")
def buzz():
	try:
		motion = ultrasonicRead(ultra)   #read distance value from ultrasonic and store in a variable 'motion'
		print(motion)
  		if motion <= 10:		#if the distance value is less than or equal to 10 the buzzer gives a sound
			digitalWrite(buzzer, 1)
		#	print("Buzzer Start")
		elif (motion > 10):
			digitalWrite(buzzer, 0)   #if the distance value is greater than 10 then buzzer stops buzzing
		#	print("Buzzer Stop")
	except KeyboardInterrupt:
		digitalWrite(buzzer, 0)
	except IOError:
		print("I/O Error")
	finally:
		return str(motion)

# in the following case, we are defining
# the function to be called when accessing
# the root URL
@app.route("/")
def getStatus():
 try:
  [temp, hum] = dht(sensor, 0)
  print(temp)
  # create a collection (in this case one variable) to store
  # the temperature and the ultrasonic distance value (which is stored in a variable 'motion') information. This collection will be used
  # rendering HTML using the render_template function
  templateData = {
   'temp': temp,
   'motion': buzz()
  }

   # one of the useful features of flask is the template rendering
   # It is based on the Jinja2 template engine which means that one
   # can combine HTML and program code (e.g. Python) which can be
   # rendered directly. The usefulness of this is that is it not easy
   # to use scripts like Python to output HTML (e.g. lots of print
   # statements) and this makes inefficient. Hence, rendering simplifies
   # this process. We can also pass, for example, variables (or collection
   # of variables to the HTML file and their values will then bind to HTML
   # elements. This means that we can then control the values of these
   # variables from the Python script.
  return render_template('gauge.html', **templateData)
 except Exception as e:
  print('an error has occured {0}'.format(str(e)))

# Flask uses the run() function to run the application on the local server
# you can specify the host, port, debug and options. If you do not specify
# the port, then the default port of the localhost:5000
# The Debug mode automate the reloading of the server if the source code changes
# That is, if the server is running and you modify this script and save it, the
# the server automatically is reloaded.
# The host by default is 127.0.0.1. If set to 0.0.0.0 this indicates that the server
# can be available externally
if __name__ == '__main__':
  app.run(debug=True, port=1200, host='0.0.0.0')

