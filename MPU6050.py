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
                self.__x_acel = struct.unpack('<f',struct.pack('4b', *datos[0:4]))[0]
                self.__y_acel = struct.unpack('<f',struct.pack('4b', *datos[5:9]))[0]
                self.__z_acel = struct.unpack('<f',struct.pack('4b', *datos[10:14]))[0]
                self.__x_gyro = struct.unpack('<f',struct.pack('4b', *datos[15:19]))[0]
                self.__y_gyro = struct.unpack('<f',struct.pack('4b', *datos[20:24]))[0]
                #self.__z_gyro = struct.unpack('<f',struct.pack('4b', *datos[25:29]))[0]
                self.__flag_datos = 1                

        def print_datos(self):
                print self.__x_acel
                print self.__y_acel
                print self.__z_acel
                print self.__x_gyro
                print self.__y_gyro
                print self.__z_gyro

        def obtener_datos(self):
                self.send(chr(103))
                while not self.__flag_datos:
                        pass
                self.__flag_datos = 0
                self.print_datos()
                self.arreglo_datos.append(self.__x_acel)
                self.arreglo_datos.append(self.__y_acel)
                self.arreglo_datos.append(self.__z_acel)
                self.arreglo_datos.append(self.__x_gyro)
                self.arreglo_datos.append(self.__y_gyro)
                self.arreglo_datos.append(self.__z_gyro)                
                return self.__arreglo_datos
