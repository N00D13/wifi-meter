#!/usr/bin/env python2.7
import subprocess
import re
import time
import smbus


#Define Device adresses
DEVICE_0 = 0x38                           
DEVICE_1 = 0x39
DEVICE_2 = 0x3A

#Open SMBus on /dev/i2c-1
bus = smbus.SMBus(1)		#0=/dev/i2c-0; 1=/dev/i2c-1


#This function manage and controls the leds
#and calc. the values for the portexpander  
def setLedBar(i):

	print(i)
	
	if i>8:
		print "DEV_0: 255"
		bus.write_byte(DEVICE_0, 0xff)
		i-=8
		
		if i>8:
			print "DEV_1: 255"
			bus.write_byte(DEVICE_1, 0xff)
			i-=8

			if i>=8:
				print "DEV_2: 255"
				bus.write_byte(DEVICE_2, 0xff)
				
			else:
				i=(2**i)-1
				print "DEV_2:",i
				bus.write_byte(DEVICE_2, i)

		else:
	                i=(2**i)-1
	                print "DEV_1:",i
			bus.write_byte(DEVICE_1, i)
			print "DEV_2:",0
			bus.write_byte(DEVICE_2, 0)
	else:
		i=(2**i)-1
		print "DEV_0:",i
		bus.write_byte(DEVICE_0, i)
		print "DEV_1:",0
		bus.write_byte(DEVICE_1, 0)
		print "DEV_2:",0
		bus.write_byte(DEVICE_2, 0)
		
		
while True:
	#Starting the iwlist process.
	proc = subprocess.Popen('iwlist  scan 2>/dev/null', shell=True, stdout=subprocess.PIPE, )
	
	stdout_str = proc.communicate()[0]
	stdout_list=stdout_str.split('\n')
	
	#EssID and Adress Array's
	essid=[]
	address=[]
	
	#For each Access Point you got information about the Channel ESSID etc.
	for line in stdout_list:
    		line=line.strip()
    		match=re.search('ESSID:"(\S+)"',line)
    		if match:
        		essid.append(match.group(1))
    		match=re.search('Address: (\S+)',line)
    		if match:
        		address.append(match.group(1)) 

	""" 
	For Debuging

	Printing the Value's
	"""

	print essid
	print address
	
	print "Aviable Adress"
	print len(address)

	print "Aviable Essid's"
	print len (essid)
	
	#Call function to control and set the leds
	setLedBar(len(essid))

	  	
