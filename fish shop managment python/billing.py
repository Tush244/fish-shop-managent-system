from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x500+250+130")
        self.root.title("Fish Billing")
        #Image1
        img=Image.open("milos-prelevic-65busv7PmzM-unsplash.jpg")
        img=img.resize((1230,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=1230,height=130)

        lbl_title=Label(self.root,text="Nitin Fish Marchant Niphad",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=100,width=1230,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=170,width=1230,height=620)

        #customer Labelframe
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=360,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",15,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",15,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=10,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,font=("arial",15,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=10,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Product LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=390,y=5,width=360,height=140)





if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

