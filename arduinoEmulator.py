import random

class Arduino:

    def __init__ ( self ):
        self.__flag_in_frame     = False
        self.__flag_flen         = False
        self.RANDOM_THRS         = 0.1
        self.RANDOM_MODE         = 0
        self.FIX_MODE            = 1
        self.ERROR_STEP          = 6
        self.TOTAL_STEPS         = 100
        self.contador            = 0
        self.__arduino_id        = 10
        self.__flen              = 0
        self.__in_data           = []
    
    def receive(self,character):
        ## Se bloquea  el metodo  hasta que entran  datos o  vence el
        ## timeout si fue seteado.
        #in_data_0      = character
        #in_data_1      = in_data_0 + self.__ser.read(self.__ser.inWaiting())
        self.__in_data.append(character)#self.__in_data + [ord(n) for n in in_data_1]
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
            #print  self.datos
            return  self.datos

    def send(self,data,device):
        header = 160;
        iheader = 64;
        data_len = len(data)
        uid = data.pop(data_len - 1)
        data_len = len(data)
        #print data_len
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
        #print str(lista)
        return lista

    def acel_model(self):
        data_total = 11
        bits_to_send = 4
        data_acel = []
        for j in range(data_total):
            random_value = random.random()/10.0 + (1.0*(j==2))
            for i in range(bits_to_send):
                data_acel.append(ord(str(random_value)[i]))
            data_acel.append(ord(' '))
        data_acel.append(self.__arduino_id)
        return data_acel
    
    def ultr_model(self):
        pass
    
    def answer_model (self):
        self.contador = (self.contador + 1) % self.TOTAL_STEPS
        data_answ = []
        if ( (random.random()<self.RANDOM_THRS and self.RANDOM_MODE) or (self.contador == self.ERROR_STEP and self.FIX_MODE)):
            data_answ.append(ord(str(1)))
        else:
            data_answ.append(ord(str(0)))
        print data_answ
        #print len(data_answ)
        data_answ.append(ord(' '))
        data_answ.append(self.__arduino_id)
        return data_answ
        
