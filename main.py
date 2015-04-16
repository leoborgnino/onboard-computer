import Comunicacion
import time
import threading
import Planing

com = Comunicacion.Comunicacion('/dev/ttyS0',115200)
com.open()

hilo_recepcion = ThreadHandler(com.receive, "Hilo de recepcion")
hilo_envio = ThreadHandler(com.send, "Hilo de envio")
open_threads()
pl = Planing()
Planing.run()
com.txfifo("defghijklmn")
time.sleep(5)	
close_threads()

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


