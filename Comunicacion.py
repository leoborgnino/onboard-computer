import threading
import Queue
import time
import sys


from ThreadHandler import ThreadHandler
import UART

class Comunicacion():

	def __init__(self,dev,baud_rate):
		self.__uart =UART.UART(dev,baud_rate)
		self.__scheduler = Scheduler.Scheduler()
		self.q_envio = Queue.Queue()
			

	def send(self):
		if(!(self.q_envio.empty())):
			self.dato = q_envio.get()
			self.uart.send(dato)
	
	def receive(self):
		self.uart.receive()	

	def reg(self,x):
		return self.__scheduler.reg(x)
	
	def txfifo(self,dato):
		q.put(dato)
