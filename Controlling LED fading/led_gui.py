#**********************#
#This program will control the brightness and the state of the LEDs using sliders and buttons by using guizero module
#**********************#
# Author : Deeksha & Navya #
# Date   : Jan 25,2020     #
#**********************#

#importing necessary libraries
import tkinter as tk
from guizero import App, Box, Text, TextBox, PushButton, Slider
from grovepi import *
import time
 
#Initialization
myLed1 = 5 					#Connect a green LED sensor to digital port 5 (D5)
myLed2 = 3 					#Connect a blue LED sensor to digital port 3 (D3)
myLed3 = 6 					#Connect a red LED sensor to digital port 6 (D6)
pinMode(myLed1, "OUTPUT") 			#set the D5 pinMode to output
pinMode(myLed2, "OUTPUT") 			#set the D3 pinMode to output
pinMode(myLed3, "OUTPUT") 			#set the D6 pinMode to output

#This function is to stop the execution of the program
def exitProgram():
	digitalWrite(myLed1, 0) 		#turn the LED OFF while exiting
	digitalWrite(myLed2, 0)
	digitalWrite(myLed3, 0)
	app.destroy()

#In this function, according to the slider value the  intensity of the LEDs will be adjusted
def sliderToggleLED1(slider_value1):
	analogWrite(myLed1, int(slider_value1))
	bind_button1(slider_value1)

def sliderToggleLED2(slider_value2):
	analogWrite(myLed2, int(slider_value2))
	bind_button2(slider_value2)

def sliderToggleLED3(slider_value3):
	analogWrite(myLed3, int(slider_value3))
	bind_button3(slider_value3)

#In this function, based on the Slider_value the button gets ON or OFF 
def bind_button1(slider_value1):
	if int(slider_value1) == 0:
		ledButton1.text = "Turn ON" 	#set the text on the button to "Turn ON"
		ledButton1.bg = "red"       	#set the background of the button to RED color
		textLED1.color = "black"    	#set the font color to black
	else:
		ledButton1.text = "Turn OFF"  	#set the text on the button to "Turn OFF"
		ledButton1.bg = "green"	      	#set the background of the button to green color
		textLED1.color = "white"      	#set the font color to white 

def bind_button2(slider_value2):
	if int(slider_value2) == 0:
		ledButton2.text = "Turn ON"
		ledButton2.bg = "red"
		textLED2.color = "black"
	else:
		ledButton2.text = "Turn OFF"
		ledButton2.bg = "green"
		textLED2.color = "white"

def bind_button3(slider_value3):
	if int(slider_value3) == 0:
		ledButton3.text = "Turn ON"
		ledButton3.bg = "red"
		textLED3.color = "black"
	else:
		ledButton3.text = "Turn OFF"
		ledButton3.bg = "green"
		textLED3.color = "white"

#In this function, according to the button status the slider value gets changed or updated.
def led1Toggle():
	button_status = digitalRead(myLed1)  	#get the status of the LED
	if (button_status != 0):	     	#check if LED status
		digitalWrite(myLed1, 0)
		ledButton1.text = "Turn ON"
		ledButton1.bg = "red"
		textLED1.color = "black"
		sliderLED1.value = 0       	#Sets the slider position according to the status
	else:
		digitalWrite(myLed1, 1)
		ledButton1.text = "Turn OFF"
		ledButton1.bg = "green"
		textLED1.color = "white"
		sliderLED1.value = 255

def led2Toggle():
	button_status = digitalRead(myLed2)
	if (button_status != 0):
		digitalWrite(myLed2, 0)
		ledButton2.text = "Turn ON"
		ledButton2.bg = "red"
		textLED2.color = "black"
		sliderLED2.value = 0
	else:
		digitalWrite(myLed2, 1)
		ledButton2.text = "Turn OFF"
		ledButton2.bg = "green"
		textLED2.color = "white"
		sliderLED2.value = 255

def led3Toggle():
	button_status = digitalRead(myLed3)
	if (button_status != 0):
		digitalWrite(myLed3, 0)
		ledButton3.text = "Turn ON"
		ledButton3.bg = "red"
		textLED3.color = "black"
		sliderLED3.value = 0
	else:
		digitalWrite(myLed3, 1)
		ledButton3.text = "Turn OFF"
		ledButton3.bg = "green"
		textLED3.color = "white"
		sliderLED3.value = 255

#Initialize the GUI application
app = App(title = "TCSS573: IoTActivity2", height = 300, width = 500)          					#sets the dimensions of the GUI
main = Text(app,text = "Led Fading" , size = 14, font = "Times New Roman", color = "navy")    			#setting the title, font, color,size of text
box = Box(app, layout = "grid" , grid = [1,0])                                                			#Initializing the container and setting the widgets

#Setting up the GUI in desired format
textLED1 = Text(box, text = "Green", align = "left", grid = [2,0])               				#It specifies the name of the corresponding LED
ledButton1 = PushButton(box, command = led1Toggle, text = "Turn ON",grid = [0,0]) 				#Creating a button according to the coordinates and calling the led1Toggle function on button click
sliderLED1 = Slider(box,start = 0, end = 255, command = sliderToggleLED1  , grid = [1,0])  			#creating a button according to the coordinates and calling the sliderToggleLED1 function when the slider is moved 

textLED2 = Text(box, text = "Blue", align = "left", grid = [2,1])
ledButton2 = PushButton(box, command = led2Toggle, text = "Turn ON",grid = [0,1])
sliderLED2 = Slider(box,start = 0, end = 255, command = sliderToggleLED2  , grid = [1,1])

textLED3 = Text(box, text = "Red", align = "left", grid = [2,2])
ledButton3 = PushButton(box, command = led3Toggle, text = "Turn ON",grid = [0,2])
sliderLED3 = Slider(box,start = 0, end = 255, command = sliderToggleLED3  , grid = [1,2])

exitButton = PushButton(box, command = exitProgram, text = "Exit", grid = [1,3])  				#creating a button to the coordinates and calling the exitProgram function on button click
app.display()    												#Displays the formatted GUI application
