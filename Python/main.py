from tkinter import ttk
from tkinter import Tk
from tkinter import *
import serial.tools.list_ports

window = Tk()
window.geometry("360x150")
window.title("Arduino Color Driver")
window.resizable(False, False)
frm = ttk.Frame(window, padding=10)
frm.grid()

ttk.Label(frm, text="Red: ").grid(column=0, row=0)
sliderRed = Scale(frm, from_=0, to=100, orient=HORIZONTAL, bg="RED").grid(column=1, row=0)

ttk.Label(frm, text="Green: ").grid(column=0, row=1)
sliderGreen = Scale(frm, from_=0, to=100, orient=HORIZONTAL, bg="GREEN").grid(column=1, row=1)

ttk.Label(frm, text="Blue: ").grid(column=0, row=2)
sliderBlue = Scale(frm, from_=0, to=100, orient=HORIZONTAL, bg="BLUE").grid(column=1, row=2)

ports = serial.tools.list_ports.comports()
portArray = []
for port, desc, hwid in sorted(ports):
        portArray.append(port)
ttk.Label(frm, text="Port: ").grid(column=3, row=0)
variable = StringVar(window)
variable.set(portArray[0]) # default value
w = OptionMenu(frm, variable, *portArray).grid(column=4, row=0)

connectButton = Button(frm, text="Connect").grid(column=4, row=1)


window.mainloop()
