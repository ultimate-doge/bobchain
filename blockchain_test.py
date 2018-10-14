from blockchain import Blockchain
from tkinter import *
usernames=a=open("Username.txt",'r').read().split('\n').pop()
passwords=a=open("Password.txt",'r').read().split('\n').pop()
main=Tk()
local_blockchain = Blockchain()
local_blockchain.print_blocks()
status="login"
def login_check():
    global username
    global password
    login_success=False
    login_index=usernames.index(username.get())
    if password.get()==passwords[login_index]:
        login_success=True
    print("login attempted"+str(login_success))
def login_attempt():
    print(login_check())
def cancel_login():
    print("login cancelled")
def login(fram):
    global username
    global password
    if fram=="login":
        pass
    elif fram=="status":
        pass
    elif fram=="transaction":
        pass
    label1=Label(main,text="Username").grid(row=0,column=0)
    label2=Label(main,text="Password").grid(row=1,column=0)
    username=Entry(main).grid(row=0,column=1)
    password=Entry(main).grid(row=1,column=1)
    loginAttempt=Button(main,text="Log In",command=login_attempt).grid(row=3,column=0)
    cancelLogin=Button(main,text="Cancel",command=cancel_login).grid(row=3,column=1)
login("login")
main.mainloop()