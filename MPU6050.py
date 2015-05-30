from Obj_Head import Obj_Head
import struct
import math

class mpu6050(Obj_Head):

        def __init__(self,com):
        
                Obj_Head.__init__(self,com,self.save)
                self.x_rotation  = 0
                self.y_rotation  = 0
                self.__x_gyro      = 0
                self.__y_gyro      = 0
                self.__z_gyro      = 0
                self.__x_acel      = 0
                self.__y_acel      = 0
                self.__z_acel      = 0
                self.__flag_datos  = 0
                self.__arreglo_datos = []
        
        def save(self,datos):
                i = 0
                while(i < len(datos)):
                    cadena = ""
                    while(datos[i]) != 32:         
                        cadena = cadena + chr(datos[i])
                        i += 1
                    self.__arreglo_datos.append(cadena)
                    i += 1
                self.__flag_datos = 1                

        def inclinacion(self):
                self.x_rotation = math.degrees(math.atan2(self.__y_acel,math.sqrt((self.__x_acel*self.__x_acel) + (self.__z_acel * self.__z_acel))))
                self.y_rotation = -math.degrees(math.atan2(self.__x_acel,math.sqrt((self.__y_acel*self.__y_acel) + (self.__z_acel * self.__z_acel))))
  
        def print_datos(self):
                datos = ["\t\tAcelerómetro:\nEje x:","Eje y:","Eje z:","\t\tGyroscopo:\nEje x:","Eje y:","Eje z:"]
                for i in range(len(self.__areglo_datos)):
                        print "%s %lf" % (datos[i],self.__arreglo_datos[i])
                print "\t\tInclinacion:\nEje x: %lf\nEje y: %lf" % (self.x_rotation, self.y_rotation)
        
        def calibrar(self):
                self.send(chr(104))

        def obtener_datos(self):
                self.send(chr(103))
                while not self.__flag_datos:
                        pass
                self.__flag_datos = 0
                self.__x_acel = self.__arreglo_datos[0]
                self.__y_acel = self.__arreglo_datos[1]
                self.__z_acel = self.__arreglo_datos[2]
                self.__x_gyro = self.__arreglo_datos[3]
                self.__y_gyro = self.__arreglo_datos[4]
                self.__z_gyro = self.__arreglo_datos[5]               
                self.inclinacion()
                self.print_datos()
                return self.__arreglo_datos
