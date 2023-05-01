
from atexit import register
from errno import EILSEQ
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from dashboard import  FMS
#from register import Register
import sqlite3

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("K.K.Wgh College Chandori BCS Project")
        self.root.geometry("1550x800+0+0")

          # IMAGE IMPORT
        image1=Image.open(r"C:\Users\USER\tushar244\GettyImages-931270318-43ab672.jpg")
        image1=image1.resize((1550,800),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(image1)
        lbling=Label(self.root,image=self.photoimage1,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=800)
        
        frame=Frame(self.root,bg="lightgrey",bd=5,relief=RIDGE)
        frame.place(x=1050,y=125,width=400,height=100)
        get_str=Label(frame,text="Login",font=("times new roman",25,"bold"),fg="black",bg="lightgrey")
        get_str.place(x=80,y=25)

        frame1=Frame(self.root,bg="lightgrey",bd=5,relief=RIDGE)
        frame1.place(x=1050,y=235,width=400,height=400)
        username=lbl=Label(frame1,text="Username",font=("times new roman",20,"bold"),fg="black",bg="lightgrey")
        username.place(x=15,y=45)
        self.textuser=Entry(frame1,font=("times new roman",15))
        self.textuser.place(x=160,y=50,width="200")

        Password=lbl=Label(frame1,text="Password",font=("times new roman",20,"bold"),fg="black",bg="lightgrey")
        Password.place(x=15,y=100)
        self.textpassword=Entry(frame1,font=("times new roman",15))
        self.textpassword.place(x=160,y=105,width="200")

        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),borderwidth=3,fg="red",bg="lightgrey")
        loginbtn.place(x=100,y=175,width="200")

        registerbtn=Button(frame1,text="Create new account",font=("times new roman",15,"bold"),borderwidth=3,fg="blue",bg="lightgrey")
        registerbtn.place(x=100,y=240,width="200")

        forgetpasswordbtn=Button(frame1,text="Forget Password",font=("times new roman",15,"bold"),borderwidth=3,fg="blue",bg="lightgrey")
        forgetpasswordbtn.place(x=100,y=300,width="200")

    def login(self):
        self.new_window=Toplevel(self.root)
        self.app=FMS(self.new_window)
        
    def login(self):
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="tushar" and self.textpassword.get()=="tushar@244":
            #messagebox.showinfo("success","welcome to the nitin fish marchant")
            self.new_window=Toplevel(self.root)
            self.app=FMS(self.new_window)
        else:
            messagebox.showerror("invalid","invalid user name and password")
    
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="tushar" and self.textpassword.get()=="tushar@244":
            #messagebox.showinfo("success","welcome to the nitin fish marchant")
            self.new_window=Toplevel(self.root)
            self.app=FMS(self.new_window)
        else:
            messagebox.showerror("invalid","invalid user name and password")
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="tushar" and self.textpassword.get()=="tushar@244":
            #messagebox.showinfo("success","welcome to the nitin fish marchant")
            self.new_window=Toplevel(self.root)
            self.app=FMS(self.new_window)
        else:
            messagebox.showerror("invalid","invalid user name and password")
    
"""    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)"""

if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

