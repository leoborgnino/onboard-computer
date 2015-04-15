import Comunicacion
import time
import threading

com = Comunicacion.Comunicacion('/dev/ttyS0',115200)
com.open()

self.hilo_recepcion = ThreadHandler(com.receive, "Hilo de recepcion")
self.hilo_envio = ThreadHandler(com.send, "Hilo de envio")
open_threads()
com.send("defghijklmn",10)
time.sleep(5)
com.close()
	

def open_threads(self):
        self.hilo_recepcion.start()
       	time.sleep(0.05)
	self.hilo_envio.start()
	time.sleep(0.05)       

def close_threads(self):
	self.hilo_recepcion.stop_thread()
	time.sleep(0.05)
	self.hilo_envio.stop_thread()
	time.sleep(0.05)          


