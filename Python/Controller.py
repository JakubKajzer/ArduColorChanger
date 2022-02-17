import serial
import View

class AppController:

    s=serial.Serial

    def connect(portName):
        if View.AppView.connectButton.cget('text') == "Connect":
            AppController.s = serial.Serial(portName,115200)
            AppController.s.write("000000".encode())
            View.AppView.isConnected()
        else:
            View.AppView.isDisconnected()
            AppController.s.close()
          
        
    def updateValue(self):
        binRed = round(2.55*View.AppView.getRedSlider())
        binGreen = round(2.55*View.AppView.getGreenSlider())
        binBlue = round(2.55*View.AppView.getBlueSlider())
        print(binRed)
        print(binGreen)
        print(binBlue)
