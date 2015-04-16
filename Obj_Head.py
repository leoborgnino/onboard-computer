class Obj_Head():

	__uid 	= 0
	__txfifo   = 0

	def __init__(self):
		self.set_uid(com.reg(self.method))
		self.set_txfifo(com.txfifo)
	
	def set_uid(self,uid):
		self.__uid = uid

	def set_txfifo(self,txfifo):
		self.__txfifo = txfifo
	
	def send(self,datos):
		self.__txfifo(datos,self.uid)
		
