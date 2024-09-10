import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.title("Our GUI Title")
ttk.Label(gui, text="hello").\
    grid(row=0, column=0)
ttk.Button(gui, text="ClickMe").\
    grid(row=0, column=1)
tk.Entry(gui, textvariable=tk.StringVar(value="     Enter your name")).\
    grid(row=0, column=2)
for child in gui.winfo_children(): #loop through GUI children
    child.grid_configure(padx=10, pady=10) #add x,y padding to each
gui.mainloop()