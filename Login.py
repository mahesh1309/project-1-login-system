from tkinter import *
 
from time import *
 
 
root=Tk()
 
root.geometry("1350x700+0+0")
 
root.title("Login system")
 
root.configure(bg="Green")
 
lbl=Label(root,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE)
 
lbl.place(x=0,y=0,relwidth=1)
 
fr=LabelFrame(lbl,bg="red").place(x=400,y=150)
 
 
def yeah():
 
    sleep(0.5)
 
    root.destroy()
 
    root1=Tk()
 
    root1.geometry("1350x780+0+0")
 
    root1.title("Login system")
 
    root1.configure(bg="green")
 
    lbl=Label(root1,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE)
 
    lbl.place(x=0,y=0,relwidth=1)
 
                    
 
    def thank():
 
        sleep(1)
 
        root1.destroy()
 
        roots=Tk()
 
        roots.geometry("1350x780+0+0")
 
        roots.title("Maheshtech")
 
        roots.configure(bg="green")
 
        lbl=Label(roots,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",30,"bold"),relief=GROOVE)
 
        lbl.place(x=0,y=0,relwidth=1)
 
        Message(roots,text="Thanks for logging in",font=(28),bg="Yellow",width=1250).place(x=200,y=200)
 
        Message(roots,text="Stay tuned for further Updates",font=(28),bg="yellow",width=1250).place(x=200,y=250)
 
        Message(roots,text="- Mahesh Reddy Kommasani",bg="cyan",font=(30),width=1250).place(x=300,y=300)
 
        roots.mainloop()
 
    
 
    user=Label(root1,text="Username",bg="White",font=(20)).place(x=200,y=150)
 
    useren=Entry(root1,bg="White",font=(20)).place(x=300,y=150)
 
    passw=Label(root1,text="Password",bg="White",font=(20)).place(x=200,y=200)
 
    passen=Entry(root1,bg="White",font=(20)).place(x=300,y=200)
 
    login=Button(root1,text="Login",font=(20),bg="skyblue",width=7,command=thank).place(x=350,y=300)
 
    chekbox=Checkbutton(root1,text="Keep me logged in",bg="Green").place(x=300,y=250)
 
    root.mainloop()
 
 
def nope():
 
 
    root=Tk()
 
    root.title("Registration")
 
    root.geometry("1350x780+0+0")
 
    root.configure(bg="green")
 
    lbl=Label(root,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE)
 
    lbl.place(x=0,y=0,relwidth=1)
 
 
    def exit():
 
        sleep(1)
 
        root.destroy()
 
 
    name=Label(root,text="Name",bg="White",font=(20),fg="black").place(x=200,y=150)
 
    nameen=Entry(root,bg="White",font=(20)).place(x=300,y=150)
 
    userre=Label(root,text="Username",bg="White",font=(20)).place(x=200,y=200)
 
    userreen=Entry(root,bg="White",font=(20)).place(x=300,y=200)
 
    passwre=Label(root,text="Password",bg="White",font=(20)).place(x=200,y=250)
 
    passreen=Entry(root,bg="White",font=(20)).place(x=300,y=250)
 
    msg=Message(root,text="Note :If account was successfully created then window will be closed automatically",width=1850,bg="green").place(x=250,y=350)
 
    cnfrm=Button(root,text="Confirm",bg="skyblue",font=(20),width=7,command=exit).place(x=250,y=300)
 
 
    root.mainloop()
 
 
 
accs=Label(root,text="Do you have an account in Maheshtech ?",font=(25)).place(x=300,y=300)
 
ss=Button(root,text="Yes",bg="White",font=(25),command=yeah).place(x=300,y=350)
 
nn=Button(root,text="No",bg="White",font=(25),command=nope).place(x=350,y=350)
 
 
root.mainloop()
