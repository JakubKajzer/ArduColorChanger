from tkinter import ttk
from tkinter import *
import serial.tools.list_ports
from functools import partial

import Controller

class AppView:
    
    

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
        self.sliderRed = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="RED").grid(column=1, row=0)

        ttk.Label(self.frm, text="Green: ").grid(column=0, row=1)
        self.sliderGreen = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="GREEN").grid(column=1, row=1)

        ttk.Label(self.frm, text="Blue: ").grid(column=0, row=2)
        self.sliderBlue = Scale(self.frm, from_=0, to=100, orient=HORIZONTAL, bg="BLUE").grid(column=1, row=2)

        self.refreshPorts()

        ttk.Label(self.frm, text="Port: ").grid(column=3, row=0)
        self.droplist = OptionMenu(self.frm, self.variable, *self.portArray).grid(column=4, row=0)

        self.connectButton = Button(self.frm, text="Connect", command=partial(Controller.AppController.connect,self.variable.get())).grid(column=4, row=1)

        self.window.mainloop()



        
