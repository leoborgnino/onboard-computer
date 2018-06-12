# fakeSerial.py
# D. Thiebaut
# A very crude simulator for PySerial assuming it
# is emulating an Arduino.
import arduinoEmulator

# a Serial class emulator
class Serial:

    ## init(): the constructor.  Many of the arguments have default values
    # and can be skipped when calling the constructor.
    def __init__( self, port='COM1', baudrate = 19200, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0):
        self.arduino_emulator = arduinoEmulator.Arduino()
        self.name     = port
        self.port     = port
        self.timeout  = timeout
        self.parity   = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff  = xonxoff
        self.rtscts   = rtscts
        self._isOpen  = True
        self._receivedData = ""
        self._data = []

    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen( self ):
        return self._isOpen

    ## open()
    # opens the port
    def open( self ):
        self._isOpen = True

    ## close()
    # closes the port
    def close( self ):
        self._isOpen = False

    ## write()
    # writes a string of characters to the Arduino
    def write( self, string ):
        #print( "Arduino got: %d "%ord(string)  )
        answer = self.arduino_emulator.receive(ord(string))
        if (answer != None):
            #print answer
            if (answer[0] == 103):
                data = self.arduino_emulator.acel_model()
                #print data
                data_to_send = self.arduino_emulator.send(data,0)
                #print len(data_to_send)
                for i in range(len(data_to_send)):
                    self._data.append(chr(data_to_send[i]))
                #print len(self._data)
            elif (answer[0] == 107):
                data = self.arduino_emulator.answer_model()
                data_to_send = self.arduino_emulator.send(data,2)
                print data_to_send
                for i in range(len(data_to_send)):
                    self._data.append(chr(data_to_send[i]))
                print self._data
    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read( self, n=1 ):
        s = self._data[0:n]
        self._data = self._data[n:]
        #print( "read: now self._data = ", self._data )
        return s

    ## readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline( self ):
        returnIndex = self._data.index( "\n" )
        if returnIndex != -1:
            s = self._data[0:returnIndex+1]
            self._data = self._data[returnIndex+1:]
            return s
        else:
            return ""

    def inWaiting(self):
        return len(self._data)

    ## __str__()
    # returns a string representation of the serial class
    def __str__( self ):
        return  "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % ( str(self.isOpen), self.port, self.baudrate ) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)"\
               % ( self.bytesize, self.parity, self.stopbits, self.xonxoff,
                   self.rtscts )
