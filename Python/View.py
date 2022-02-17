from tkinter import ttk
from tkinter import *
from unicodedata import name
import serial.tools.list_ports
from functools import partial

import Controller

class AppView:
    
    droplist = OptionMenu
    connectButton = Button

    sliderRed = Scale
    sliderGreen = Scale
    sliderBlue = Scale

    def refreshPorts(self):
        ports = serial.tools.list_ports.comports()
        self.portArray.clear()
    
        for port, desc, hwid in sorted(ports):
            self.portArray.append(port)
        self.variable.set(self.portArray[0])


    def __init__(self):
        self.window = Tk()
        self.window.geometry("360x150")
        self.window.title("Arduino Color Driver")
        self.window.resizable(False, False)

        self.frm = ttk.Frame()
        self.frm.master=self.window
        self.frm.grid()

        self.portArray = []
        self.variable = StringVar(self.window)

        ttk.Label(self.frm, text="Red: ").grid(column=0, row=0)
        AppView.sliderRed = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="RED", command=Controller.AppController.updateValue)
        
        AppView.sliderRed.grid(column=1, row=0)

        ttk.Label(self.frm, text="Green: ").grid(column=0, row=1)
        AppView.sliderGreen = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="GREEN", command=Controller.AppController.updateValue)
        AppView.sliderGreen.grid(column=1, row=1)

        ttk.Label(self.frm, text="Blue: ").grid(column=0, row=2)
        AppView.sliderBlue = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="BLUE", command=Controller.AppController.updateValue)
        AppView.sliderBlue.grid(column=1, row=2)

        self.refreshPorts()

        ttk.Label(self.frm, text="Port: ").grid(column=3, row=0)
        AppView.droplist = OptionMenu(self.frm, self.variable, *self.portArray)
        AppView.droplist.grid(column=4, row=0)
        AppView.connectButton = Button(self.frm, text="Connect", command=partial(Controller.AppController.connect,self.variable.get()))
        AppView.connectButton.grid(column=4, row=1)
        self.window.mainloop()
    
    def getRedSlider():
        return int(AppView.sliderRed.get())

    def getGreenSlider():
        return int(AppView.sliderGreen.get())

    def getBlueSlider():
        return int(AppView.sliderBlue.get())

    def isConnected():
        AppView.droplist.configure(state='disabled')
        AppView.connectButton.configure(text='Disconnect')

    def isDisconnected():
        AppView.droplist.configure(state='normal')
        AppView.connectButton.configure(text='Connect')



        
