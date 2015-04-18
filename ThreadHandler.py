#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading 
import time

class ThreadHandler(threading.Thread):
    """La idea de esta clase es manejar los hilos independiente de eventos"""
    
    def __init__(self,method, th_name):
        threading.Thread.__init__(self,name=th_name)
        self.method      = method
        self.onoff       = True
        #self.wait_time   = wait_time

    def run(self):
        print self.getName(),"""[Listening]"""
        
        while True:

            if self.onoff:
                #time.sleep(self.wait_time)
                self.method()
            else:
                break
        
        print self.getName(),"""[Finished]"""

    def stop_thread(self):
        self.onoff = False
    	if self.isAlive():
        	try:
            		self._Thread__stop()
        	except:
            		print(str(self.getName()) + ' could not be terminated')	

