import threading
import Queue
import time
import sys


from ThreadHandler import ThreadHandler
import UART
import Scheduler

class Comunicacion():

	def __init__(self,dev,baud_rate):
		self.__uart  = UART.UART(dev,baud_rate)
		self.__scheduler = Scheduler.Scheduler()
		self.q_envio = Queue.Queue()
			

	def send(self):
		if not (self.q_envio.empty()):
			self.dato = self.q_envio.get()
			self.__uart.send(self.dato)
	
	def receive(self):
<<<<<<< HEAD
		self.__uart.receive(self.__scheduler)	
=======
		self.uart.receive(self.__scheduler.mngr)	
>>>>>>> ddbfb7f887bc428be646e20169b9a6e57746bf69

	def reg(self,x):
		return self.__scheduler.reg(x)
	
	def txfifo(self,dato,uid):
		lista = []
		lista.append(dato)
		lista.append(uid)		
		self.q_envio.put(lista)
