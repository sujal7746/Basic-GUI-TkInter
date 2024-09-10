import  tkinter as tk
from tkinter import  ttk
gui = tk.Tk()
gui.title("GUI APP")
frame = ttk.LabelFrame(gui, text="A frame surrounding widget") #gui is parent of frame
frame.pack(padx= 10, pady = 5)

#frame is parent
ttk.Label(frame, text="hello").\
    grid(row=0, column=0)
ttk.Button(frame, text="ClickMe").\
    grid(row=0, column=1)
tk.Entry(frame, textvariable=tk.StringVar(value="     Enter your name")).\
    grid(row=0, column=2)
for child in gui.winfo_children(): #loop through GUI children
    child.grid_configure(padx=10, pady=10) #add x,y padding to each
gui.mainloop()