import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault") 

def loginScreen():
    window.geometry("250x100")

    lbl= Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt= Entry(window, width=20)
    txt.pack()
    
    btn= Button(window, text="Submit")
    btn.pack()

loginScreen()
window.mainloop()