import UART
import time

com = UART.UART('/dev/ttyS0',115200)

com.send("defghijklmn",10)
