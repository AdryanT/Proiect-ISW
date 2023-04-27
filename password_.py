import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial
import uuid
import pyperclip
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


#Database Code
with sqlite3.connect("password_vault.db") as db:
	cursor= db.cursor()
	
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL),
recoveryKey TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

#Create PopUP
def popUp(text):
    answer= simpledialog.askstring("intput string", text)
	
    return answer
	
#Window
window = Tk()

window.title("Password Vault") 

def hashPassword(input):
    hash = hashlib.sha256(intup)
    hash = hash.hexdigest()
	
    return hash

def firstScreen():
	for widget in window.winfo_children():
		widget.destroy()
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
    
def recoveryScreen(key):
	for widget in window.winfo_children():
		widget.destroy()
		
		
	 window.geometry("250x150")
    lbl= Label(window, text="Save this key to be able to recover account")
    lbl.config(anchor=CENTER)
    lbl.pack()
lbl= Label(window, text=key)
    lbl.config(anchor=CENTER)
    lbl.pack()

def copyKey():
	pyperclip.copy(lbl1.get("text"))

def done():
	vaultScreen()

    btn= Button(window, text="Done", command=done )
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
    btn.pack(pady=5)
    
    btn= Button(window, text="Reset", command=resetPassword)
    btn.pack(pady=5)
    
    
def passwordVault();
    for widget in window.winfo_children():
	widget.destroy();
	
    def addEntry():
	text1="Website"
	text2="Website"
	text3="Website"
	
	website = popUp(text1)
	username = popUp(text2)
	password = popUp(text3)
	
	insert_fields = """INSERT INTO vault(website,username,password) 
	VALUES(?,?,?)"""
	
	cursor.execute(insert_fields, (website,username, password))
	db.commit()
	
	passwordVault()
	
    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
	db.commit()

    window.geometry("750x350")
	
    lbl = Label(window, text="Password Vault")
    lbl.grid(column=1, padY=10)
	
    btn = Button(window, text="+", command=addEntry)
    btn.grid(column=1, padY=10)
	
    lbl= Label(window, text="Website")
    lbl.grid(row=2,colum=0, padx=80
	     

   cursor.execute("SELECT * FROM vault")
   if (cursor.fetchall() != None):
	     i=0
	     while True:
	     cursor.execute("SELECT * FROM vault")
	     array = cursor.fetchall()
	     
	     lbl1 = Label(window, text= ( array[i][1], font=("Helvetica", 12))
	     lbl1.grid(column=0, row= i+3)
	     lbl1 = Label(window, text= ( array[i][2], font=("Helvetica", 12))
	     lbl1.grid(column=1, row= i+3)
	     lbl1 = Label(window, text= ( array[i][3], font=("Helvetica", 12))
	     lbl1.grid(column=2, row= i+3)
			  
	btn = Button(window, text= "Delete", command = partial(removeEntry, array[i][0]))
	button.grid(collumn=3, row = i+3, pady=10)
			  
	i= i+1
			  
	cursor.execute("SELECT * FROM vault")
	if(len(cursor.fetchall()) <=i):
			  break

check = cursor.execute("SELECT * FROM masterpassword")
if check:
    loginScreen()
else
    firstScreen()

window.mainloop()
