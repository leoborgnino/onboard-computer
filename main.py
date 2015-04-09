import UART
import time

com = UART.UART('/dev/ttyS0',115200)

com.send("defghijklmn",10)

data = com.receive()

for i in data:
	print i
