import subprocess
from subprocess import Popen, PIPE
import threading
import time
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:24:14 2012

@author: slarinier
"""

class Screenshots(threading.Thread):
	def __init__(self,listofwebsites,jsfile,location,website):
		self.listofwebsites=listofwebsites
		self.jsfile=jsfile
		self.location=location
		self.website=website
		threading.Thread.__init__(self)
		
	
	def run(self):
		cmd='casperjs '+self.jsfile+' '+self.website +' http://'+self.website +' '+self.location+' --web-security=no'
		args=cmd.split()
		result=subprocess.Popen(args,stdout=PIPE)
		print "Make screenshots :"+self.website
		time.sleep(3)			
	
