from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from loginu import Login_Window
import mysql.connector


class Register:
    def __init__(self,root):
            self.root=root
            self.root.title("Register")
            self.root.geometry("1550x800+0+0")

              # IMAGE IMPORT
            image1=Image.open(r"C:\Users\USER\tushar244\GettyImages-931270318-43ab672.jpg")
            image1=image1.resize((1550,800),Image.ANTIALIAS)
            self.photoimage1=ImageTk.PhotoImage(image1)
            lbling=Label(self.root,image=self.photoimage1,relief=RIDGE)
            lbling.place(x=0,y=0,width=1550,height=800)


            frame=Frame(self.root,bg="lightgrey",bd=5,relief=RIDGE)
            frame.place(x=50,y=160,width=345,height=470)

            get_str=Label(frame,text="New",font=("times new roman",35,"bold","underline"),fg="black",bg="lightgrey")
            get_str.place(x=120,y=125)
            get_str=Label(frame,text="Registration",font=("times new roman",35,"bold","underline"),fg="black",bg="lightgrey")
            get_str.place(x=50,y=180)

            frame1=Frame(self.root,bg="lightgrey",bd=5,relief=RIDGE)
            frame1.place(x=400,y=160,width=650,height=470)

            fname=Label(frame1,text="First name :-",font=("times new roman",20,"bold"),bg="lightgrey")
            fname.place(x=50,y=20)
            fname_entry=ttk.Entry(frame1,font=("times new roman",15))
            fname_entry.place(x=50,y=60,width="200",height="30")

            lname=Label(frame1,text="Last name :-",font=("times new roman",20,"bold"),bg="lightgrey")
            lname.place(x=50,y=100)
            self.text_lname=ttk.Entry(frame1,font=("times new roman",15))
            self.text_lname.place(x=50,y=140,width="200",height="30")

            contact=Label(frame1,text="Contact no. :-",font=("times new roman",20,"bold"),bg="lightgrey")
            contact.place(x=50,y=180)
            self.text_contact=ttk.Entry(frame1,font=("times new roman",15))
            self.text_contact.place(x=50,y=220,width="200",height="30")

            email=Label(frame1,text="Email :-",font=("times new roman",20,"bold"),bg="lightgrey")
            email.place(x=50,y=260)
            self.text_email=ttk.Entry(frame1,font=("times new roman",15))
            self.text_email.place(x=50,y=300,width="200",height="30")

            ssque=Label(frame1,text="Select Security Quetion :-",font=("times new roman",20,"bold"),bg="lightgrey")
            ssque.place(x=300,y=20)
            
            self.combo_security_que=ttk.Combobox(frame1,font=("times new roman",15),state="readonly")
            self.combo_security_que["values"]=("Select","Which is your Birth place ?","What is your Birth date ?","Which is your favorite game ?","What is your pet name ?")
            self.combo_security_que.place(x=300,y=60,width="300")
            self.combo_security_que.current(0)

            sans=Label(frame1,text="Security Answer :-",font=("times new roman",20,"bold"),bg="lightgrey")
            sans.place(x=300,y=100)
            self.text_sans=ttk.Entry(frame1,font=("times new roman",15))
            self.text_sans.place(x=300,y=140,width="300",height="30")

            password=Label(frame1,text="Password :-",font=("times new roman",20,"bold"),bg="lightgrey")
            password.place(x=300,y=180)
            self.text_password=ttk.Entry(frame1,font=("times new roman",15))
            self.text_password.place(x=300,y=220,width="300",height="30")

            cpassword=Label(frame1,text="Confirm Password :-",font=("times new roman",20,"bold"),bg="lightgrey")
            cpassword.place(x=300,y=260)
            self.text_cpassword=ttk.Entry(frame1,font=("times new roman",15))
            self.text_cpassword.place(x=300,y=300,width="300",height="30")

           # ==========check button===========

            checkbtn=Checkbutton(frame1,text="I Agree The Terms & Conditions",font=("times new roman",13),onvalue=1,offvalue=0)
            checkbtn.place(x=50,y=350)
            

            #==============Button===========

            b1=Button(frame1,text="Register Now",font=("times new roman",18,"bold"),borderwidth=3,fg="black",bg="white")
            b1.place(x=50,y=390,width="200")

            b2=Button(frame1,text="Login Now",font=("times new roman",18,"bold"),borderwidth=3,fg="black",bg="white")
            b2.place(x=300,y=390,width="200")

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)


if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
