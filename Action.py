from tkinter import ttk
import tkinter as tk

gui = tk.Tk()
gui.title("Our GUI Title")
frame = ttk.LabelFrame(gui, text="A frame surrounding widget") #gui is parent of frame
frame.pack(padx= 10, pady = 5)

ttk.Label(frame, text="hello").\
    grid(row=0, column=0)

def button_callback():
    entry.config(textvariable= tk.StringVar(value= '    Button is clicked'))
ttk.Button(frame, text="ClickMe", command=button_callback).\
    grid(row=0, column=1)
entry = tk.Entry(frame, textvariable=tk.StringVar(value="     Enter"))
entry.grid(row=0, column=2)
for child in frame.winfo_children(): #loop through GUI children
    child.grid_configure(padx=10, pady=10) #add x,y padding to each
gui.mainloop()