
from math import *
import random
import Obj_Head

class Planing(Obj_Head):

	grid		=    	    [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
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

	goal = [0, 0]
	init = [len(grid)-1, len(grid[0])-1]
	tita = 0
	contador = 0	

	def __init__(self):
		Obj_Head.__init__(self)
		self.path = plan(self,grid, init, goal)		
	
	def run(self):

		self.path.astar()
		for i  in range(len(self.path.path) - 1):
			self.paso = self.path.action[self.path.path[i+1][0]][self.path.path[i+1][1]]
			self.rotacion = (self.paso - self.tita) * 90
			if self.rotacion > 180:
				self.rotacion = self.rotacion - 360
			if self.rotacion < -180:
				self.rotacion = self.rotacion + 360
		
			self.send(paso)			
			self.send(rotacion)
			#print("%s.Rotar %s grados" % (i,rotacion))
			#print 'Adelante 30 cm'
			#print("%s.Enviado: %s" % (i,rotacion) )
		
			self.tita = self.tita + (self.paso-self.tita)
			if self.tita > 4:
				self.tita = 0
			if self.tita < -1:
				self.tita = 3	
