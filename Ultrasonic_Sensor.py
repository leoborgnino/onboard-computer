from Obj_Head import Obj_Head
import struct
import math

class Ultrasonic_Sensor(Obj_Head):

        def __init__(self,com):

                Obj_Head.__init__(self,com,self.save)
                self.__ultrasonic_distance = [0]*120
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
            for i in range(120/6):
                datos = [chr(105)] + [chr(i)]
                self.send(datos)
                while not self.__flag_datos:
                    pass
                self.__flag_datos = 0
                self.__ultrasonic_distance[i*6  ] = self.__arreglo_datos[0]
                self.__ultrasonic_distance[i*6+1] = self.__arreglo_datos[1]
                self.__ultrasonic_distance[i*6+2] = self.__arreglo_datos[2]
                self.__ultrasonic_distance[i*6+3] = self.__arreglo_datos[3]
                self.__ultrasonic_distance[i*6+4] = self.__arreglo_datos[4]
                self.__ultrasonic_distance[i*6+5] = self.__arreglo_datos[5]
            print self.__arreglo_datos
            return self.__arreglo_datos
