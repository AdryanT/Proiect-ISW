import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Vault") 

def firstScreen():
    window.geometry("250x150")

    lbl= Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()
	
    txt= Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.pack()
	
    txt1= Entry(window, width=20)
    txt1.pack()
    txt1.focus()

def savePassword():
	print("test")

    btn= Button(window, text="Save", command=savePassword )
    btn.pack(pady=10)

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
            passwordVault()
        else:
	    txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")

    btn= Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)
    
    def passwordVault();
	for widget in window.winfo_children():
	widget.destroy();
	window.geometry("750x350")
	
	lbl = Label(window, text="Password Vault")
	lbl.config(anchor=CENTER)
    	lbl.pack()

firstScreen()
window.mainloop()
