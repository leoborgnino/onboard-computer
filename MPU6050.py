from Obj_Head import Obj_Head
import struct
import math

class mpu6050(Obj_Head):

        def __init__(self,com):
        
                Obj_Head.__init__(self,com,self.save)
                self.x_rotation    = 0
                self.y_rotation    = 0
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
                self.x_rotation = math.degrees(math.atan2(float(self.__y_acel),math.sqrt((float(self.__x_acel)*float(self.__x_acel)) + (float(self.__z_acel) * float(self.__z_acel)))))
                self.y_rotation = -math.degrees(math.atan2(float(self.__x_acel),math.sqrt((float(self.__y_acel)*float(self.__y_acel)) + (float(self.__z_acel) * float(self.__z_acel)))))
  
        def print_datos(self):
                print "\nAcelerometro: \t\tGiroscopo: \t\tInclinacion:"
		print "--------------\t\t-----------\t\t------------"
                print "Eje x: %s \t\tEje x: %s \t\tEje x: %s" % (self.__x_acel,self.__x_gyro,self.x_rotation)  
		print "Eje y: %s \t\tEje y: %s \t\tEje y: %s" % (self.__y_acel,self.__y_gyro,self.y_rotation) 
        	print "Eje z: %s \t\tEje z: %s" % (self.__z_acel,self.__z_gyro)
	def calibrar(self):
		print "Calibracion [OK]"
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
                return self.__arreglo_datos
