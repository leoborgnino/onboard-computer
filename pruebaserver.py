import web
from Obj_Head import Obj_Head

urls = ('/','index')

class index(Obj_Head):
	
	def GET(self):
		self.send("g")
		while not self.__flag_recibido:
			pass
	        self.__flag_recibido = 0
        	return str(self.__datos[0]) + " " + str(self.__datos[1])
	
	def __init__(self,com):
		self.__flag_recibido = 0
		self.__datos = []
		Obj_Head.__init__(self,com,self.datos_rec)
                app= web.application(urls,globals())
                app.run()
		
	def datos_rec(self,datos):
		for i in range(len(datos)/6):
			dat_temp = ""
			for j in range(6):
				dat_temp = dat_temp + datos[j + (i * 6)]
			self.__datos.append(float(dat_temp))
		print "DATOS RECIBIDOS"
		self.__flag_recibido = 1
			
