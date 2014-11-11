#!/usr/bin/env python2.7

import smbus 

DEVICE_0 = 0x38                           
DEVICE_1 = 0x39
DEVICE_2 = 0x3A


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
			bus.write_byte(DEVICE_1 , i)

	else:
		i=(2**i)-1
		print "DEV_0:",i
		bus.write_byte(DEVICE_0, i)


bus = smbus.SMBus(1)		# 0=/dev/i2c-0;  1=/dev/i2c-1


#Example
setLedBar(13)
