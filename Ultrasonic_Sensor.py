from Obj_Head import Obj_Head
import struct
import math

class Ultrasonic_Sensor(Obj_Head):

        N_STEPS = 120

        def __init__(self,com):
                Obj_Head.__init__(self,com,self.save)
                self.__ultrasonic_distance = [0]*self.N_STEPS
                self.__flag_datos  = 0
                self.__arreglo_datos = []

        def save(self,datos):
                i = 0
                self.__arreglo_datos = []
                while(i < len(datos)):
                    cadena = ""
                    while(datos[i]) != 32:
                        cadena = cadena + chr(datos[i])
                        i += 1
                    if cadena != "":
		    	self.__arreglo_datos.append(cadena)
                    i += 1
                print self.__arreglo_datos
                self.__flag_datos = 1

        def obtener_datos(self):
            for i in range(self.N_STEPS/6):
                datos = [chr(105)] + [chr(i)]
                self.send(datos)
                while not self.__flag_datos:
                    pass
                self.__flag_datos = 0
                self.__ultrasonic_distance[i*6  ] = float(self.__arreglo_datos[0])/100
                self.__ultrasonic_distance[i*6+1] = float(self.__arreglo_datos[1])/100
                self.__ultrasonic_distance[i*6+2] = float(self.__arreglo_datos[2])/100
                self.__ultrasonic_distance[i*6+3] = float(self.__arreglo_datos[3])/100
                self.__ultrasonic_distance[i*6+4] = float(self.__arreglo_datos[4])/100
                self.__ultrasonic_distance[i*6+5] = float(self.__arreglo_datos[5])/100
           #print self.__arreglo_datos
            return self.__ultrasonic_distance
