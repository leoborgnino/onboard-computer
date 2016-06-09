import web
urls = ('/','index')

class index:	
	def GET(self):
		return pruebaserver.datos()

class pruebaserver:
	def __init__(self,acelerometro):
		self.acelerometro = acelerometro
		app = web.application(urls,globals())
		app.run()
	def datos():
		return acelerometro.x_inclinacion + " " + acelerometro.y_inclinacion
			
