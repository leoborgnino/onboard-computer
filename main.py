import Comunicacion
import time
import threading
import Planing
import ThreadHandler
import pruebaserver
import MPU6050

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
hilo_recepcion = ThreadHandler.ThreadHandler(com.receive, "Hilo de recepcion")
hilo_envio = ThreadHandler.ThreadHandler(com.send, "Hilo de envio")
open_threads()
acelerometro = MPU6050.mpu6050(com)
acelerometro.obtener_datos()
#pl = Planing.Planing(com)
#web = pruebaserver.index(com)
#pl.run()
#com.txfifo("defghijklmn")
#time.sleep(5)
close_threads()



