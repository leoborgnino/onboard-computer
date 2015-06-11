import Comunicacion
import time
import threading
import Planing
import ThreadHandler
#import pruebaserver
import MPU6050
#import graphic

def open_threads():
	hilo_recepcion.start()
	time.sleep(0.05)
	hilo_envio.start()
	time.sleep(0.05)       

def close_threads():
	hilo_recepcion.stop_thread()
	time.sleep(0.05)
	hilo_envio.stop_thread()
	time.sleep(0.05)          

com = Comunicacion.Comunicacion('/dev/ttyS0',115200)
acelerometro = MPU6050.mpu6050(com)
hilo_recepcion = ThreadHandler.ThreadHandler(com.receive, "Hilo de recepcion")
hilo_envio = ThreadHandler.ThreadHandler(com.send, "Hilo de envio")
open_threads()
acelerometro.calibrar()
time.sleep(1)
acelerometro.obtener_datos()
acelerometro.print_datos()
pl = Planing.Planing(com)
#web = pruebaserver.pruebaserver(acelerometro)
pl.run()
#com.txfifo("defghijklmn")
#time.sleep(5)
print "Run OP"


close_threads()



