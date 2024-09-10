import tkinter as tk
from tkinter import ttk

gui = tk.Tk()

ttk.Label(gui, text="hello").\
    grid(row=0, column=0)
ttk.Button(gui, text="ClickMe").\
    grid(row=0, column=1)
tk.Entry(gui, textvariable=tk.StringVar(value="     Enter your name")).\
    grid(row=0, column=2)
gui.mainloop()