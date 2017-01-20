#########################################################################################
##  Main smart car                                                                      #
##                                                                                      #
##  execute in terminal: python main.py sys.argv[1] sys.argv[2]                         #
##                                                                                      #
##  sys.argv[1] = name of the serial port to use. Example: /dev/ttyUSB0                 #
##  sys.argv[2] = name of the image to import and use in the planing                    #
##                                                                                     #
#########################################################################################

import Comunicacion
import time
import threading
import Planing
import ThreadHandler
import MPU6050
import Ultrasonic_Sensor
import graphic
import sys

BAUD_RATE = 9600

def open_threads():
    hilo_recepcion.start()
    time.sleep(0.05)
    hilo_envio.start()
    time.sleep(0.05)
#    hilo_grafico.start()
#    time.sleep(0.05)

def close_threads():
    hilo_recepcion.stop_thread()
    time.sleep(0.05)
    hilo_envio.stop_thread()
    time.sleep(0.05)
#    hilo_grafico.stop_thread()
#    time.sleep(0.05)

com = Comunicacion.Comunicacion(sys.argv[1],BAUD_RATE)
acelerometro = MPU6050.mpu6050(com)
ultrasonido = Ultrasonic_Sensor.Ultrasonic_Sensor(com)
grafico = graphic.grafico(acelerometro,ultrasonido)
#grafico = graphic.grafico(acelerometro)
hilo_recepcion = ThreadHandler.ThreadHandler(com.receive, "Hilo de recepcion")
hilo_envio = ThreadHandler.ThreadHandler(com.send, "Hilo de envio")
#hilo_grafico = ThreadHandler.ThreadHandler(grafico.run, "Hilo Grafico")
open_threads()
acelerometro.calibrar()
acelerometro.obtener_datos()
acelerometro.print_datos()
pl = Planing.Planing(com,sys.argv[2])
pl.run()
time.sleep(50)
close_threads()
