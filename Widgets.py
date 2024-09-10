import tkinter as tk #alias tkinter as 'tk'
from tkinter import ttk #tkk == 'themed tk"
gui = tk.Tk() #create Tk() instance and assign as variable
ttk.Label(gui, text="hello Label").\
    grid(row=0, column=0)             #create a themed tk label
ttk.Button(gui, text='click me').\
    grid(row=1 , column= 1) #gui is the parent for the widgets
tk.Entry(gui).\
    grid(row=2, column=2)  #using grid layout manager taking entry

gui.mainloop()