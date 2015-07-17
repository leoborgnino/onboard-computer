from scipy import misc
from math import *
import random
from Obj_Head import Obj_Head
import plan
import time


class Planing(Obj_Head):

	def __init__(self,com,imagen):
		self.grid		=    	    [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
		   	  	                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
		     	              	     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
			                         [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
			                         [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
			 	                     [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
				                     [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
	                     	         [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
			                         [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
			                         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
			                         [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
			                         [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
	                     	         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

		self.goal = [0, 0]
		self.init = [len(self.grid)-1, len(self.grid[0])-1]
		self.tita = 0
		self.contador = 0	
		Obj_Head.__init__(self,com,self.flag)
		self.path = plan.plan(self.grid,self.init,self.goal)		
		self.__flag = 0
	
	def run(self):
		contador = 1
		self.path.astar()
		for i  in range(len(self.path.path) - 1):
			self.paso = self.path.action[self.path.path[i+1][0]][self.path.path[i+1][1]]
			self.rotacion = (self.paso - self.tita) * 90
			if self.rotacion > 180:
				self.rotacion = self.rotacion - 360
			if self.rotacion < -180:
				self.rotacion = self.rotacion + 360

			if self.rotacion != 0:				
				#if (contador * 30) > 240:
				#	while (contador*30) > 90:
				#		datos = [chr(100)] + [chr(90)] + [chr(70)] + [chr(0)]
				#		self.send(datos)
				#		self.__flag = 0
				#		while not self.__flag:
				#			pass
				#		self.__flag = 0	
				#		contador = contador - 3
				
				datos = [chr(102)] + [chr(abs(self.rotacion))] + [chr(1) if self.rotacion > 0 else chr(0)] 
				self.send(datos)
				while not self.__flag:
					pass
				self.__flag = 0
				datos = [chr(100)] + [chr(30)] + [chr(70)] + [chr(0)]
				#contador = 0			    
				self.send(datos)
				while not self.__flag:
					pass
				self.__flag = 0
			else:
				datos = [chr(100)] + [chr(30)] + [chr(70)] + [chr(0)]
				#contador = 0			    
				self.send(datos)
				while not self.__flag:
					pass
				self.__flag = 0

			self.__flag = 0
			#print("%s.Rotar %s grados" % (i,rotacion))
			#print 'Adelante 30 cm'
			#print("%s.Enviado: %s" % (i,rotacion) )
		
			self.tita = self.tita + (self.paso-self.tita)
			if self.tita > 4:
				self.tita = 0
			if self.tita < -1:
				self.tita = 3
				
	def flag(self,datos):
		self.__flag = 1
