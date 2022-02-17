import serial
import View

class AppController:

    def connect(portName):
        s = serial.Serial(portName,115200)
        s.write("0000FF".encode())
        View.AppView.droplist.configure(state='disabled')
        s.close()
