from tkinter import*
from PIL import Image,ImageTk
from customer import customerclass
from employee import employeeclass
from f_category import f_categoryclass
from f_product import f_productclass
from supplier import supplierclass
from stock import stockclass
#from xyz import Bill_App




class fishManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Lodging Management System") 
        self.root.geometry("1550x800+0+0")


        # IMAGE IMPORT
        image1=Image.open(r"C:\Users\USER\tushar244\GettyImages-931270318-43ab672.jpg")
        image1=image1.resize((1550,800))
        self.photoimage1=ImageTk.PhotoImage(image1)
        lbling=Label(self.root,image=self.photoimage1,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=800)

        
        # IMAGE IMPORT
        image2=Image.open(r"C:\Users\USER\tushar244\GettyImages-931270318-43ab672.jpg")
        image2=image2.resize((240,300))
        self.photoimage2=ImageTk.PhotoImage(image2)
        lbl=Label(self.root,image=self.photoimage2,relief=RIDGE)
        lbl.place(x=0,y=560,width=240,height=230)

        #FRAME 
        lblframe=Frame(self.root,bg="black",bd=7,relief=RIDGE)
        lblframe.place(x=0,y=20,width=1530,height=120)
        get_str=Label(lblframe,text="Fish shop Management System",font=("times new roman",45,"bold","italic"),fg="gold",bg="black")
        get_str.place(x=450,y=15)

        #MENU
        menuframe=Label(self.root,text="Menu",font=("times new roman",20,"bold","italic"),bg="black",fg="Gold",bd=4,relief=RIDGE)
        menuframe.place(x=0,y=150,width=240,height=50)

         #BUTTON FRAME 
        btnframe=Frame(self.root,bg="black",bd=4,relief=RIDGE)
        btnframe.place(x=0,y=205,width=240,height=380)

        ebtn=Button(btnframe,text="Employee",command=self.employee,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        ebtn.place(x=7,y=20)

        cbtn=Button(btnframe,text="Customer",command=self.customer,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        cbtn.place(x=7,y=80)

        stbtn=Button(btnframe,text="Stock",command=self.Stock,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        stbtn.place(x=7,y=140)

        fcatbtn=Button(btnframe,text="f_category",command=self.f_category,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        fcatbtn.place(x=7,y=200)

        fprdbtn=Button(btnframe,text="f_product",command=self.f_product,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        fprdbtn.place(x=7,y=260)
        
        fspbtn=Button(btnframe,text="Supplier",command=self.supplier,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        fspbtn.place(x=7,y=320)

        #billbtn=Button(btnframe,text="Bill",command=self.Report,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        #billbtn.place(x=7,y=200)

        lobtn=Button(btnframe,text="Logout",command=self.logout,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        lobtn.place(x=7,y=380)

        #lobtn=Button(btnframe,text="Bill",command=self.Bill,width=17,font=("times new roman",16,"bold","italic"),bg="lightgrey",fg="black",bd=4)
        #lobtn.place(x=7,y=260)

       


    def employee(self):
        self.new_window=Toplevel(self.root)
        self.app=employeeclass(self.new_window)

    
    def customer(self):
        self.new_window=Toplevel(self.root)
        self.app=customerclass(self.new_window) 

    def Stock(self):
        self.new_window=Toplevel(self.root)
        self.app=stockclass(self.new_window)

    def f_category(self):
        self.new_window=Toplevel(self.root)
        self.app=f_categoryclass(self.new_window)

    def f_product(self):
        self.new_window=Toplevel(self.root)
        self.app=f_productclass(self.new_window)

    def supplier(self):
        self.new_window=Toplevel(self.root)
        self.app=supplierclass(self.new_window)


    """def Bill(self):
        self.new_window=Toplevel(self.root)
        self.app=Bill_App(self.new_window)"""
       
    def logout(self):
        self.root.destroy()





if __name__=="__main__":
    root=Tk()
    obj=fishManagementSystem(root)
    root.mainloop()
