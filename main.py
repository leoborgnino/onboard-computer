import Comunicacion
import time
import graphic

com = Comunicacion.Comunicacion('/dev/ttyS0',115200)
com.open()
com.send("defghijklmn",10)
time.sleep(5)
com.close()

grafico = graphic.grafico()
grafico.run()

while True:
	pass
