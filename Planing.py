
from math import *
import random
from Obj_Head import Obj_Head
import plan

class Planing(Obj_Head):
	def __init__(self,com):
		self.grid		=   [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
			     	             [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
		     		             [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			        	     [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
			            	     [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
			 	     	     [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
				             [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
	                     	    	     [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
			             	     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			             	     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			           	     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
			 	     	     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
	                     	     	     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],


class Planing(Obj_Head):

	def __init__(self):
	    self.goal = [0, 0]
	    self.init = [len(grid)-1, len(grid[0])-1]
	    self.tita = 0
	    self.contador = 0	
	    self.path = plan(self,grid, init, goal)		
	    self.grid		=    	    [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
		     	                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
		     	                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
			 	             [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
				             [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
	                     	             [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			                     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
			 	             [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
	                     	             [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
			                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
	                     	             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

		self.goal = [0, 0]
		self.init = [len(self.grid)-1, len(self.grid[0])-1]
		self.tita = 0
		self.contador = 0	
		Obj_Head.__init__(self,com,self.flag)
		self.path = plan.plan(self.grid,self.init,self.goal)		
		self.flag = 0
	
	def run(self):
		self.path.astar()
		for i  in range(len(self.path.path) - 1):
			self.paso = self.path.action[self.path.path[i+1][0]][self.path.path[i+1][1]]
			self.rotacion = (self.paso - self.tita) * 90
			if self.rotacion > 180:
				self.rotacion = self.rotacion - 360
			if self.rotacion < -180:
				self.rotacion = self.rotacion + 360
		
			self.send(self.paso)			
			self.send(self.rotacion)
			while not self.flag:
				pass
			self.flag = 0
			#print("%s.Rotar %s grados" % (i,rotacion))
			#print 'Adelante 30 cm'
			#print("%s.Enviado: %s" % (i,rotacion) )
		
			self.tita = self.tita + (self.paso-self.tita)
			if self.tita > 4:
				self.tita = 0
			if self.tita < -1:
				self.tita = 3	
	def flag(self):
		self.__flag = 1
