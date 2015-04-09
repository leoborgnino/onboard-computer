class Protocolo:   
                   
	def encode(self,device, data):
        	header   = 160;
        	iheader  = 64;
        	data_len = len(data)

	        if data_len>2**20:
	            return []
	        else:
	            if data_len<16:
	                PL          = 0;
	                mod_header  = header  + PL + data_len 
	                mod_iheader = 64
	                size_l      = 0;
	                size_h      = 0;
	            
	            else:
	                PL          = 16
	                mod_header  = header  + PL + ((data_len & 0xf0000)>>16)
	                mod_iheader = 64
	                size_l      = data_len & 0xff
	                size_h      = (data_len & 0xff00)>>8
		    lista = [mod_header,size_h,size_l,device]
		    for i in data:
			lista = lista + [i]
		    lista = lista + [mod_iheader] 
		    print lista     
	            return  lista
