class Scheduler:

	def __init__(self):
		self.__obj = []
		self.__contador_id = -1
		pass

	def reg(self,method):
		#probar
		self.__obj.append(method)
		self.__contador_id = self.__contador_id + 1
		return self.__contador_id
	
	def mngr(self,id_obj,datos):
		print ",,,"
		self.__obj[id_obj](datos)		
