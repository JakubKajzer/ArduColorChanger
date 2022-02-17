import serial
import View

class AppController:

    s=serial.Serial

    def connect(portName):
        if View.AppView.connectButton.cget('text') == "Connect":
            AppController.s = serial.Serial(portName,115200)
            View.AppView.isConnected()
        else:
            View.AppView.isDisconnected()
            AppController.s.close()
          
        
    def updateValue(self):
        if View.AppView.connectButton.cget('text') == "Disconnect":
            binRed = round(2.55*View.AppView.getRedSlider())
            binGreen = round(2.55*View.AppView.getGreenSlider())
            binBlue = round(2.55*View.AppView.getBlueSlider())
            valueToSend="%02X%02X%02X" % (binRed, binGreen, binBlue)
            if AppController.s.isOpen():
                AppController.s.write(valueToSend.encode())
