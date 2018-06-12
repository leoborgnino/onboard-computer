import threading
import Queue
import time
import sys


from ThreadHandler import ThreadHandler
import UART
import Scheduler

class Comunicacion():

	def __init__(self,dev,baud_rate,sim_mode):
		self.__uart  = UART.UART(dev,baud_rate,sim_mode)
		self.__scheduler = Scheduler.Scheduler()
		self.q_envio = Queue.Queue()

	def send(self):
		if not (self.q_envio.empty()):
			self.dato = self.q_envio.get()
			self.__uart.send(self.dato)
	
	def receive(self):
		self.__uart.receive(self.__scheduler.mngr)	

	def reg(self,x):
		return self.__scheduler.reg(x)
	
	def txfifo(self,dato,uid):
		lista = []
	#	if type(dato) == int:
	#		lista.append(dato)
	#		lista.append(uid)
	#	else:
		for i in range(len(dato)):
			for j in range(len(dato[i])):
				lista.append(dato[i][j])
		lista.append(uid)		
		self.q_envio.put(lista)
