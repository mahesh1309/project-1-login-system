from tkinter import *
from tkinter import messagebox
from time import *

def main():
    f=open("maheshtechdetails.txt","a")
    root=Tk()
    root.geometry("1350x700+0+0")
    root.title("Login system")
    root.configure(bg="Green")
    lbl=Label(root,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE).place(x=0,y=0,relwidth=1)
    fr=LabelFrame(lbl,bg="red").place(x=400,y=150)

    def yeah():
        try:
            root.destroy()
        except Exception:
            pass
        root1=Tk()    
        user=StringVar()
        password=StringVar()
        root1.geometry("1350x780+0+0")
        root1.title("Login system")
        root1.configure(bg="green")
        lbl=Label(root1,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE)
        lbl.place(x=0,y=0,relwidth=1)

                    
        def thank():
            if user.get()=="" or password.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                sleep(0.5)     
                root1.destroy()
                global roots

                roots=Tk()
                roots.geometry("1350x780+0+0")
                roots.title("Maheshtech")
                roots.configure(bg="green")
                lbl=Label(roots,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",30,"bold"),relief=GROOVE)
                lbl.place(x=0,y=0,relwidth=1)
                Message(roots,text="Thanks for logging in",font=(28),bg="Yellow",width=1250).place(x=200,y=200)
                Message(roots,text="Stay tuned for further Updates",font=(28),bg="yellow",width=1250).place(x=200,y=250)
                Message(roots,text="- Mahesh Reddy Kommasani",bg="cyan",font=(30),width=1250).place(x=300,y=300)
                Message(roots,text="Hello "+user.get()+"!!!",bg="Orange",width=1250,font=(55)).place(x=500,y=100)
                logout=Button(roots,text="Logout",bg="skyblue",font=(20),command=main).place(x=1200,y=60)
                roots.mainloop()
        
        
    
        usern=Label(root1,text="Username",bg="White",font=(20)).place(x=200,y=150)
        useren=Entry(root1,bg="White",font=(20),textvariable=user).place(x=300,y=150)
        passw=Label(root1,text="Password",bg="White",font=(20)).place(x=200,y=200)
        passen=Entry(root1,bg="White",font=(20),show=("*"),textvariable=password).place(x=300,y=200)
        login=Button(root1,text="Login",font=(20),bg="skyblue",width=7,command=thank).place(x=350,y=300)
        chekbox=Checkbutton(root1,text="Keep me logged in",bg="Green").place(x=300,y=250)
        root.mainloop()

    def nope():
        sleep(0.5)
        root.destroy()
        root2=Tk()
        user=StringVar()
        password=StringVar()
        peru=StringVar()
        root2.title("Registration")
        root2.geometry("1350x780+0+0")
        root2.configure(bg="green")
        lbl=Label(root2,text="Maheshtech.Ltd",bg="cyan",fg="orange",font=("Times new roman",48,"bold"),relief=GROOVE)
        lbl.place(x=0,y=0,relwidth=1)
    
        def exit():
            if user.get()=="" or password.get()=="" or peru.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                f.write(peru.get()+" ")
                f.write(user.get()+" ")
                f.write(password.get()+"\n")
                sleep(0.5)
            
                root2.destroy()
                yeah()

        name=Label(root2,text="Name",bg="White",font=(20),fg="black").place(x=200,y=150)
        nameen=Entry(root2,bg="White",font=(20),textvariable=peru).place(x=300,y=150)
        userre=Label(root2,text="Username",bg="White",font=(20)).place(x=200,y=200)
        userreen=Entry(root2,bg="White",font=(20),textvariable=user).place(x=300,y=200)
        passwre=Label(root2,text="Password",bg="White",font=(20)).place(x=200,y=250)
        passreen=Entry(root2,bg="White",font=(20),show=('*'),textvariable=password).place(x=300,y=250)
        msg=Message(root2,text="Note :If account was successfully created then window will be closed automatically",width=1850,bg="green").place(x=250,y=350)
        cnfrm=Button(root2,text="Confirm",bg="skyblue",font=(20),width=7,command=exit).place(x=250,y=300)

        root2.mainloop()
    
   
    accs=Label(root,text="Do you have an account in Maheshtech ?",font=(25)).place(x=300,y=300)
    ss=Button(root,text="Yes",bg="White",font=(25),command=yeah).place(x=300,y=350)
    nn=Button(root,text="No",bg="White",font=(25),command=nope).place(x=350,y=350)
    try:
        roots.destroy()
    except Exception:
        pass
    root.mainloop()
    


main()
