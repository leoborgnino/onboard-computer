from Obj_Head import Obj_Head
import struct

class mpu6050(Obj_Head):

        def __init__(self,com):
        
                Obj_Head.__init__(self,com,self.save)
                self.__x_rotation  = 0
                self.__y_rotation  = 0
                self.__x_gyro      = 0
                self.__y_gyro      = 0
                self.__z_gyro      = 0
                self.__x_acel      = 0
                self.__y_acel      = 0
                self.__z_acel      = 0
                self.__flag_datos  = 0
                self.__arreglo_datos = []
        
        def save(self,datos):
                for j in range (6):
                        cadena = ""
                        for i in range(4):
                                cadena = cadena + chr(datos[i + (4*j)])        
                        self.__arreglo_datos.append(cadena)
                self.__flag_datos = 1                

        def print_datos(self):
                print self.__arreglo_datos
                
        def obtener_datos(self):
                self.send(chr(103))
                while not self.__flag_datos:
                        pass
                self.__flag_datos = 0
                self.print_datos()
                self.__x_acel = self.__arreglo_datos[0]
                self.__y_acel = self.__arreglo_datos[1]
                self.__z_acel = self.__arreglo_datos[2]
                self.__x_gyro = self.__arreglo_datos[3]
                self.__y_gyro = self.__arreglo_datos[4]
                self.__z_gyro = self.__arreglo_datos[5]               
                return self.__arreglo_datos
