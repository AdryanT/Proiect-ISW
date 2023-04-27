import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault") 

def loginScreen():
    window.geometry("250x100")

    lbl= Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window)
    lbl1.pack()

    txt= Entry(window, width=20)
    txt.pack()
    txt.focus()


    def checkPassword():
        password ="test"

        if password == txt.get():
            print("Right Password")
        else:
            lbl1.config(text="Wrong Password")

    btn= Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)
    
    def passwordVault();
	for widget in window.winfo_children():
	widget.destroy();

loginScreen()
window.mainloop()
