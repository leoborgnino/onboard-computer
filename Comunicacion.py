import threading
import time
import sys


from ThreadHandler import ThreadHandler
import UART

class Comunicacion():

	def __init__(self,dev,baud_rate):
		
		self.uart =UART.UART(dev,baud_rate)
		self.hilo_recepcion = ThreadHandler(self.uart.receive, "Hilo de recepcion")
		#Aca irian proximos hilos						
	
	def send(self,dato,dev):
		self.uart.send(dato,dev)
	
	def open(self):
	        self.hilo_recepcion.start()
        	time.sleep(0.05)
       
    	def close(self):
		self.hilo_recepcion.stop_thread()
		time.sleep(0.05)          


