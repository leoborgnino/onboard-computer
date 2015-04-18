import web
from Obj_Head import Obj_Head

urls = ('/','index')

class index:
	def GET(self):
		self.send(102)
		while not self.__flag_recibido:
			pass
	        self.__flag_recibido = 0
        	return "%f %f" % self.__datos[0], self.__datos[1]
        
	def __init__(self):
		self.__flag_recibido = 0
		self.__datos = []
		Obj_Head.__init__(self,self.set_flag)
                app= web.application(urls,globals())
                app.run()
		
	def datos_rec(self,datos):
		for i in range(len(datos)/6):
			dat_temp = ""
			for j in range(6):
				dat_temp = dat_temp + datos[j + (i * 6)]
			self.__datos.append(float(dat_temp))
		self.__flag_recibido = 1
			
