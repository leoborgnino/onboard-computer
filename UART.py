import serial
import Protocolo

class UART:

	def __init__(self,PUERTO_SERIE,BAUDRATE):	
		self.__ser = serial.Serial(PUERTO_SERIE,BAUDRATE,bytesize=8,parity='N', stopbits=1)
		self.__ser.close()
		self.__ser.open()
		self.prot = Protocolo.Protocolo()
                self.hilo_recepcion = ThreadHandler(self.UART.receive,"Hilo de Recepcion de datos")
		self.__flag_in_frame     = False
                self.__flag_flen         = False
                self.__flen              = 0
                self.__in_data           = []
		if not self.__ser.isOpen():
			print 'Error'

	def send(self,data,device):
		self.__ser.write(self.prot.encode(device,data))

	def receive(self):
	
		self.recibido = 0
		while not self.recibido:
			### Se bloquea  el metodo  hasta que entran  datos o  vence el
        		### timeout si fue seteado.
        		in_data_0      = self.__ser.read()
        		in_data_1      = in_data_0+self.__ser.read(self.__ser.inWaiting())
        		self.__in_data = self.__in_data+[ord(n) for n in in_data_1]
	
        		#print "Datos de entrada:", self.__in_data
	
        		### Si no estamos procesando una trama se busca el Marcador de
        		### Inicio de Trama (MIT).
        		if self.__flag_in_frame==False:
        	    		indx = [i for i,x in enumerate(self.__in_data) if (x&0xE0)==160]
        	    	if len(indx)>0:
        	        	self.__in_data       = self.__in_data[indx[0]:len(self.__in_data)]
        	        	self.__flag_in_frame = True
        	    	else:
        	        	self.__in_data       = []
			        ### Si encontramos un MIT y no tenemos la longitud de la trama
	        	### aguardamos hasta tener al menos  3 octetos para extraer el
		        ### parametro de longitud.
		        if self.__flag_in_frame==True and self.__flag_flen==False and len(self.__in_data)>=3:
		       	    if self.__in_data[0]&0x10:
		                self.__flen          = ((self.__in_data[0]&0xF)<<16) + \
		                                        (self.__in_data[1]<<8)       + \
		                                         self.__in_data[2]
		            else:
		                self.__flen          = self.__in_data[0]&0x0F
		            self.__flag_flen         = True
		            
		        ### Una vez con  sincronismo de trama y con la  longitud de la
		        ### misma se  espera el resto  de la trama  y se coloca  en la
		        ### cola del usuario
        		if self.__flag_in_frame==True and self.__flag_flen==True and len(self.__in_data)>= \
											  (self.__flen+5):
		            self.__from_target_queue.put(self.__in_data[0:(self.__flen+5)])
		            self.datos = self.__in_data[4:(self.__flen+4)]
		            self.__in_data      = self.__in_data[(self.__flen+5):]
		            self.__flag_in_fame = False
		            self.__flag_flen    = False
		            self.__flen         = 0
		            self.recibido 	= 1
			    print self.datos
                            return self.datos

		            
		     		
