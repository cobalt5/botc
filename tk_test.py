import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.title("feet to meters")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column = 0, row = 0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

feet = tkinter.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column = 2, row = 1, sticky=(tkinter.W, tkinter.E))
#what if we specified column = 99 or 500?

def calculate(*args):
    try:
        value  = float(feet.get())
        meters.set(round(0.3048*value, 4))
    except ValueError():
        pass

meters = tkinter.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column = 2, row = 2, sticky=(tkinter.W, tkinter.E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column = 3, row = 3, sticky=tkinter.W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tkinter.W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tkinter.E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tkinter.W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()




