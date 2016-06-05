import serial


class UART:

	def __init__(self,PUERTO_SERIE,BAUDRATE):
		self.__ser = serial.Serial(PUERTO_SERIE,BAUDRATE,bytesize=8,parity='N', stopbits=1)
		self.__ser.close()
		self.__ser.open()
		self.__flag_in_frame     = False
                self.__flag_flen         = False
                self.__flen              = 0
                self.__in_data           = []
		if not self.__ser.isOpen():
			print 'Error'

	def send(self,data):
		device = 10
		header = 160;
		iheader = 64;
		data_len = len(data)
		uid = data.pop(data_len - 1)
		data_len = len(data)
		if data_len>2**20:
			return []
		else:
			PL = 16
			mod_header = header + PL + ((data_len & 0xf0000)>>16)
			mod_iheader = 64
			size_l = data_len & 0xff
			size_h = (data_len & 0xff00)>>8
			if type(data)==list:
				lista = [mod_header,size_h,size_l,device,uid]+data+[mod_iheader]
			else:
				lista = [mod_header,size_h,size_l,device,uid]+[data]+[mod_iheader]

			for i in range(len(lista)):
				if type(lista[i]) == int:
					self.__ser.write(str(chr(lista[i])))
				else:
					self.__ser.write(str(lista[i]))
		 	#print str(lista)

	def receive(self,method):
			### Se bloquea  el metodo  hasta que entran  datos o  vence el
        		### timeout si fue seteado.
        		in_data_0      = self.__ser.read()
        		in_data_1      = in_data_0 + self.__ser.read(self.__ser.inWaiting())
        		self.__in_data = self.__in_data + [ord(n) for n in in_data_1]


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
											  (self.__flen+6):
		            self.datos = self.__in_data[5:(self.__flen+5)]
                            self.uid = self.__in_data[3]
                            self.device = self.__in_data[4]
		            self.__in_data      = self.__in_data[(self.__flen+6):]
		            self.__flag_in_frame = False
		            self.__flag_flen    = False
		            self.__flen         = 0
			    #print self.datos
                            method(self.uid,self.datos)
