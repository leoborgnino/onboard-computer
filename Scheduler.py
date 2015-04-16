class Scheduler:
	self.__contador_id = -1
	self.__obj = []

	def __init__(self):
		pass

	def reg(self,method):
		#probar
		obj.append(method)
		self.__contador_id = self.__contador_id + 1
		return self.__contador_id
	
	def mngr(self,id_obj,datos):
		self.__obj[id_obj](datos)		
