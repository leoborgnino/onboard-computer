import Comunicacion
import time

com = Comunicacion.Comunicacion('/dev/ttyS0',115200)
com.open()
com.send("defghijklmn",10)
time.sleep(5)
com.close()
