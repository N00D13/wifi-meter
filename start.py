#!/usr/bin/env python2.7
import subprocess
import re
import time

while True:
	proc = subprocess.Popen('iwlist  scan 2>/dev/null', shell=True, stdout=subprocess.PIPE, )
	stdout_str = proc.communicate()[0]
	stdout_list=stdout_str.split('\n')
	essid=[]
	address=[]
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
	"""

	print essid
	print address
	
	print "Aviable Adress"
	print len(address)

	print "Aviable Essid's"
	print len (essid)
	  	
