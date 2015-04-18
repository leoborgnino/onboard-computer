class Obj_Head(object):

<<<<<<< HEAD
	def __init__(self,com,method):
		self.set_uid(com.reg(method))
=======
	def __init__(self):
	        self.__uid 	= 0
        	self.__txfifo   = 0
		self.set_uid(com.reg(self.method))
>>>>>>> ddbfb7f887bc428be646e20169b9a6e57746bf69
		self.set_txfifo(com.txfifo)
	
	def set_uid(self,uid):
		self.__uid = uid

	def set_txfifo(self,txfifo):
		self.__txfifo = txfifo
	
	def send(self,datos):
		self.__txfifo(datos,self.__uid)
		
