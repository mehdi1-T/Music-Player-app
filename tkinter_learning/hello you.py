# import tkinter module
from tkinter import *

def welcome():
    name = nameEntry.get()
    return Label(ws, text=f'hello {name}',pady=15, bg="#567").grid(row=3, column=1)

ws = Tk()
ws.title("First Program")
ws.geometry("300x300")
ws.configure(bg="#567")

# label and entry boxes
nameLable = Label(ws, text="Enter Your Name: ", pady=15, padx=10, bg='#567')
nameEntry = Entry(ws)

welcomeButton = Button(ws, text="Click me", command=welcome)

# postion the widgets
nameLable.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
welcomeButton.grid(row=2, column=0)

# infinity loop
ws.mainloop()