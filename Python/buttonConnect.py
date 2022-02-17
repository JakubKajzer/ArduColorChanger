import serial

def connect(portName):
    s = serial.Serial(portName,115200)
    s.write("0000FF".encode())
    s.close()
