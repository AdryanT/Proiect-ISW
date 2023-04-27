import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial

#Database
with sqlite3.connect("password_vault.db") as db:
	cursor= db.cursor()
	
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

#Window
window = Tk()

window.title("Password Vault") 

def hashPassword(input):
	hash = hashlib.md5(intup)
	hash = hash.hexdigest()
	
	return hash

def firstScreen():
    window.geometry("250x150")

    lbl= Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()
	
    txt= Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.pack()
	
    txt1= Entry(window, width=20, show="*")
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()
    
def savePassword():
	if txt.get() == text1.get():
  	    hasedPassword = hashPassword(txt.get().encode("utf-8"))
	
	    insert_password = """INSERT INTO masterpassword(password)
	    VALUES(?) """
	    cursor.execute(insert_password, [(hashedPassword)])
	    db.commit()
	
 	    passwordVault()
	else:
	    lbl2.config(text="Passwords do not match")

    btn= Button(window, text="Save", command=savePassword )
    btn.pack(pady=10)

def loginScreen():
    window.geometry("250x100")

    lbl= Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window)
    lbl1.pack()

    txt= Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()
def getMasterPassword():
	checkMasterPassword = hashPassword(txt.get().encode("utf-8"))
	cursor.execute("SELECT * FROM masterpassword WHERE id= 1 AND password = ?",[(chechHashedPassword)])
	return cursor.fetchall()

    def checkPassword():
        match = getMasterPassword()

	

        if match:
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

check = cursor.execute("SELECT * FROM masterpassword")
if check:
    loginScreen()
else
    firstScreen()

window.mainloop()
